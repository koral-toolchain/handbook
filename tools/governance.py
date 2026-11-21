"""Verify policy-change scope using a pinned handbook and merged data records."""
import argparse
from fnmatch import fnmatchcase
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def critical_paths(names, policy):
    return sorted(name for name in names if any(fnmatchcase(name, pattern) for pattern in policy['criticalPaths']))


def validate_record(record, repository, issue, base, actual):
    require(record['schema'] == 'koral-policy-change/1', 'Unsupported policy record')
    require(record['repository'] == repository, 'Policy record belongs to another repository')
    require(type(record['issue']) is int and record['issue'] == issue, 'Policy issue mismatch')
    require(record['baseCommit'] == base, 'Policy record was scoped to another base commit')
    require(record['decision'] == 'accepted-maintainer-scope', 'No recorded maintainer scope decision')
    require(isinstance(record['reason'], str) and record['reason'].strip(), 'Missing scope reason')
    require(record['files'] == actual, 'Critical files or resulting bytes differ from the recorded scope')
    for name, digest in actual.items():
        path = PurePosixPath(name)
        require(not path.is_absolute() and '..' not in path.parts, 'Unsafe policy path')
        require(digest == 'deleted' or re.fullmatch('[a-f0-9]{64}', digest), 'Invalid resulting file digest')


def verify(product, records, base, head, body, repository, policy):
    for ref in [base, head]:
        require(re.fullmatch('[a-f0-9]{40}', ref), 'Use full product commit identities')
    names = git(product, 'diff', '--name-only', '--no-renames', base, head).decode().splitlines()
    governed = critical_paths(names, policy)
    if not governed:
        print('No critical policy paths changed')
        return
    issue = re.search(r'(?i)\b(?:refs|closes|fixes)\s+#([1-9][0-9]*)\b', body)
    pointer = re.search(r'^Policy-Record:\s*([a-f0-9]{40})\s*$', body, re.M)
    require(issue is not None and pointer is not None, 'Critical changes require an issue and Policy-Record commit')
    ref = pointer[1]
    # Records are data, never imported or executed. The checkout must be fetched main.
    require(subprocess.run(['git', '-C', str(records), 'merge-base', '--is-ancestor', ref, 'origin/main'],
                           capture_output=True).returncode == 0, 'Policy record is not merged into handbook main')
    number = int(issue[1])
    raw = git(records, 'show', f'{ref}:policy-changes/koral-solana/{number}.json')
    record = json.loads(raw)
    active = json.loads(git(records, 'show', f'origin/main:policy-changes/koral-solana/{number}.json'))
    require(record == active, 'Policy record was superseded or withdrawn on handbook main')
    actual = {}
    for name in governed:
        listing = git(product, 'ls-tree', head, '--', name).decode().strip()
        if not listing:
            actual[name] = 'deleted'
        else:
            require(listing.startswith(('100644 ', '100755 ')), 'Critical policy file must be a regular blob')
            actual[name] = hashlib.sha256(git(product, 'show', f'{head}:{name}')).hexdigest()
    validate_record(record, repository, number, base, actual)
    print(f'Merged policy scope matches issue #{number} and {len(actual)} exact critical files')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--product', type=Path, required=True)
    p.add_argument('--records', type=Path, required=True)
    p.add_argument('--base', required=True)
    p.add_argument('--head', required=True)
    p.add_argument('--body-file', type=Path, required=True)
    p.add_argument('--repository', required=True)
    args = p.parse_args()
    policy = json.loads((ROOT/'config/governance.json').read_text())
    verify(args.product, args.records, args.base, args.head, args.body_file.read_text(), args.repository, policy)


if __name__ == '__main__':
    main()
