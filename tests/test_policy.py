import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('policy',Path(__file__).parents[1]/'tools/policy.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)

class PolicyTests(unittest.TestCase):
    def test_accepts_explained_fix(self):
        p.check_commit('fix(runtime): reject read-only recipients\n\nReject before transfer and verify unchanged balances.')
    def test_rejects_vague_or_invalid_headers(self):
        for message in ['update','docs: update','fix(unknown): reject a bad state\n\nReason','docs: describe the guide.']:
            with self.subTest(message=message),self.assertRaises(ValueError):p.check_commit(message)
    def test_requires_fix_body(self):
        with self.assertRaises(ValueError):p.check_commit('fix(runtime): reject unsigned calls')
    def test_requires_explained_breaking_marker(self):
        with self.assertRaises(ValueError):p.check_commit('feat(language)!: change account layout\n\nLayout changes.')
        p.check_commit('feat(language)!: change account layout\n\nBREAKING CHANGE: older state needs migration.')
    def test_gate_accepts_only_complete_success(self):
        needs={x:{'result':'success'} for x in p.config()['requiredJobs']}
        p.check_gate(needs)
        for status in ['skipped','cancelled','failure',None]:
            bad=dict(needs);bad['unit']={'result':status}
            with self.subTest(status=status),self.assertRaises(ValueError):p.check_gate(bad)
        del needs['unit']
        with self.assertRaises(ValueError):p.check_gate(needs)
    def test_release_gate_requires_additional_checks(self):
        needs={x:{'result':'success'} for x in p.config()['requiredJobs']}
        with self.assertRaises(ValueError):p.check_gate(needs,stage='release')
        for name in p.config()['releaseRequiredJobs']:needs[name]={'result':'success'}
        p.check_gate(needs,stage='release')
        needs['artifact-integrity']={'result':'skipped'}
        with self.assertRaises(ValueError):p.check_gate(needs,stage='release')
    def fixture(self,root):
        files={'build.gradle.kts':'plugins { kotlin("jvm") version "2.2.21" }\nversion = "0.1.0-dev"\njvmToolchain(17)\n','compiler/build.gradle.kts':'implementation("org.jetbrains.kotlin:kotlin-compiler-embeddable:2.2.21")','gradle/wrapper/gradle-wrapper.properties':'distributionUrl=https://services.gradle.org/distributions/gradle-8.14.6-bin.zip\ndistributionSha256Sum='+p.config()['pins']['gradleSha256']+'\n','cli/src/main/kotlin/dev/koral/cli/Main.kt':'println("Koral 0.1.0-dev\\n")\n"compiler" to "koral-0.1.0-dev"','testing/package.json':json.dumps({'engines':{'node':'>=22.12'}})}
        for name,text in files.items():
            f=root/name;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(text)
    def test_accepts_matching_versions(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);self.fixture(root);self.assertEqual(p.check_versions(root)['version'],'0.1.0-dev')
    def test_rejects_compiler_version_drift(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);self.fixture(root)
            f=root/'compiler/build.gradle.kts';f.write_text(f.read_text().replace('2.2.21','2.3.0'))
            with self.assertRaises(ValueError):p.check_versions(root)
    def test_rejects_cli_version_drift(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);self.fixture(root)
            f=root/'cli/src/main/kotlin/dev/koral/cli/Main.kt';f.write_text(f.read_text().replace('Koral 0.1.0-dev','Koral 0.1.1'))
            with self.assertRaises(ValueError):p.check_versions(root)
    def test_rejects_wrapper_integrity_change(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);self.fixture(root)
            f=root/'gradle/wrapper/gradle-wrapper.properties';f.write_text(f.read_text().replace(p.config()['pins']['gradleSha256'],'0'*64))
            with self.assertRaises(ValueError):p.check_versions(root)

if __name__=='__main__':unittest.main()
