import copy
import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('governance',Path(__file__).parents[1]/'tools/governance.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)

class GovernanceTests(unittest.TestCase):
    def record(self):
        return {'schema':'koral-policy-change/1','repository':'koral-toolchain/koral-solana','issue':31,
                'baseCommit':'a'*40,'decision':'accepted-maintainer-scope','reason':'Bounded control maintenance',
                'files':{'cli/build.gradle.kts':'b'*64}}

    def test_exact_record_matches(self):
        r=self.record();g.validate_record(r,r['repository'],31,'a'*40,r['files'])

    def test_mismatched_issue_base_scope_bytes_and_decision_fail(self):
        r=self.record()
        for key,value in [('issue',32),('baseCommit','c'*40),('files',{}),('decision','title-only'),('reason','')]:
            bad=copy.deepcopy(r);bad[key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):
                g.validate_record(bad,r['repository'],31,'a'*40,r['files'])

    def test_module_and_architecture_files_are_critical(self):
        import json
        policy=json.loads((g.ROOT/'config/governance.json').read_text())
        names=['cli/build.gradle.kts','cli/src/test/kotlin/dev/koral/cli/ArchitectureTest.kt','gradle/wrapper/gradle-wrapper.properties']
        self.assertEqual(g.critical_paths(names,policy),sorted(names))
        self.assertEqual(g.critical_paths(['examples/counter.kt'],policy),[])

if __name__=='__main__':unittest.main()
