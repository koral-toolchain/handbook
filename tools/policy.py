"""Original Koral policy checks. Declarations are not runtime qualification."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def config():
    return json.loads((ROOT/'config/koral-solana.json').read_text())

def require(value, message):
    if not value:
        raise ValueError(message)

def check_commit(message, policy=None):
    policy = policy or config()
    lines = message.strip().splitlines()
    require(lines, 'Missing commit message')
    header = lines[0]
    require(len(header) <= policy['headerMax'], 'Commit header exceeds policy length')
    match = re.fullmatch(r'([a-z]+)(?:\(([a-z0-9-]+)\))?(!)?: (\S.*)', header)
    require(match, 'Expected type(scope): subject')
    kind, scope, breaking, subject = match.groups()
    require(kind in policy['allowedTypes'], 'Unknown commit type')
    require(scope is None or scope in policy['allowedScopes'], 'Unknown scope')
    require(not subject.endswith('.'), 'Subject must not end with a period')
    require(subject.lower() not in ['update','fix','fix stuff','changes','wip'], 'Describe the actual change')
    body = '\n'.join(lines[1:]).strip()
    if kind in policy['bodyRequiredTypes']:
        require(body, kind+' requires a body explaining the reason and verification')
    marker = re.search(r'^BREAKING CHANGE:\s*\S', body, re.M)
    require(bool(breaking) == bool(marker), 'Breaking changes need both ! and a BREAKING CHANGE paragraph')

def check_gate(results, policy=None, stage="pr"):
    policy = policy or config()
    require(isinstance(results, dict), 'Expected a job result object')
    failures = []
    for name in policy['releaseRequiredJobs' if stage == 'release' else 'requiredJobs']:
        value = results.get(name)
        status = value.get('result') if isinstance(value, dict) else value
        if status != 'success':
            failures.append(name+': '+str(status or 'missing'))
    require(not failures, 'Required checks did not succeed: '+', '.join(failures))

def check_versions(repo, policy=None):
    policy = policy or config()
    pins = policy['pins']
    repo = Path(repo)
    build = (repo/'build.gradle.kts').read_text()
    compiler = (repo/'compiler/build.gradle.kts').read_text()
    wrapper = (repo/'gradle/wrapper/gradle-wrapper.properties').read_text()
    cli = (repo/'cli/src/main/kotlin/dev/koral/cli/Main.kt').read_text()
    testing = json.loads((repo/'testing/package.json').read_text())
    def one(pattern, text, label):
        matches = re.findall(pattern, text, re.M)
        require(len(matches) == 1, 'Expected one explicit '+label)
        return matches[0]
    kotlin = one(r'kotlin\("jvm"\)\s+version\s+"([^"]+)"', build, 'Kotlin build version')
    embedded = one(r'kotlin-compiler-embeddable:([^"\s]+)', compiler, 'embedded compiler version')
    require(kotlin == embedded == pins['kotlin'], 'Kotlin build/embedded compiler/policy pins disagree')
    jdk = one(r'jvmToolchain\((\d+)\)', build, 'build JDK')
    require(int(jdk) == pins['buildJdk'], 'Build JDK differs from policy')
    gradle = one(r'gradle-([0-9.]+)-(?:bin|all)\.zip', wrapper, 'Gradle wrapper version')
    checksum = one(r'^distributionSha256Sum=([a-f0-9]{64})$', wrapper, 'wrapper checksum')
    require(gradle == pins['gradle'] and checksum == pins['gradleSha256'], 'Gradle wrapper/checksum differs from policy')
    version = one(r'^\s*version\s*=\s*"([^"]+)"', build, 'product version')
    cli_version = one(r'Koral ([^\s"\\]+)', cli, 'CLI identity')
    manifest_version = one(r'"compiler"\s+to\s+"koral-([^"]+)"', cli, 'build manifest version')
    require(version == cli_version == manifest_version == pins['productVersion'], 'Gradle, CLI, manifest and policy versions disagree')
    require(testing['engines']['node'] == pins['nodeMinimum'], 'Test-tool Node minimum differs from policy')
    return {'kotlin':kotlin,'gradle':gradle,'buildJdk':int(jdk),'version':version,'scope':'declaration consistency only; not a runtime matrix'}

def check_handbook(root=ROOT):
    root = Path(root)
    policy = json.loads((root/'config/koral-solana.json').read_text())
    require(policy['owner'] == 'tidemark-labs', 'Unexpected owner')
    for key in ['requiredJobs','releaseRequiredJobs']:
        require(len(policy[key]) == len(set(policy[key])) > 0, 'Required jobs must be unique and non-empty')
    require(set(policy['requiredJobs']).issubset(policy['releaseRequiredJobs']), 'Release gates must retain PR gates')
    require(policy['proposedQualification']['qualifiedMatrixAlreadyExecuted'] is False, 'Do not mark the proposed matrix executed without actual evidence and policy revision')
    require((root/'.github/CODEOWNERS').read_text().strip() == '* @tidemark-labs', 'Unexpected code owner')
    broken=[]
    for file in root.rglob('*.md'):
        if '.git' in file.parts:
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)\s]+)\)', file.read_text()):
            parsed=urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            if not (file.parent/unquote(parsed.path)).exists():
                broken.append(str(file.relative_to(root))+': '+target)
    require(not broken, 'Broken handbook links: '+', '.join(broken))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('handbook')
    c=sub.add_parser('commit');c.add_argument('--message-file',required=True)
    g=sub.add_parser('gate');g.add_argument('--needs-file',required=True);g.add_argument('--stage',choices=['pr','release'],default='pr')
    v=sub.add_parser('versions');v.add_argument('--repo',required=True)
    args=parser.parse_args()
    if args.command=='handbook':check_handbook()
    elif args.command=='commit':check_commit(Path(args.message_file).read_text())
    elif args.command=='gate':check_gate(json.loads(Path(args.needs_file).read_text()),stage=args.stage)
    else:print(json.dumps(check_versions(args.repo)))
    print('Policy check passed:',args.command)

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,OSError) as error:
        print('POLICY FAILURE: '+str(error),file=sys.stderr);sys.exit(1)
