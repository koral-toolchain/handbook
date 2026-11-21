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


class GovernanceGitTests(unittest.TestCase):
    def test_merged_exact_record_passes_but_unmerged_and_changed_record_fail(self):
        import hashlib
        import json
        import subprocess
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);product=root/'product';records=root/'records'
            for repo in [product,records]:
                repo.mkdir();subprocess.run(['git','init','-b','main',str(repo)],check=True,capture_output=True)
                g.git(repo,'config','user.name','Fixture');g.git(repo,'config','user.email','fixture@example.invalid')
            def commit(repo):
                g.git(repo,'add','.');g.git(repo,'commit','-m','Fixture');return g.git(repo,'rev-parse','HEAD').decode().strip()
            file=product/'cli/build.gradle.kts';file.parent.mkdir();file.write_text('original')
            base=commit(product);file.write_text('reviewed');head=commit(product)
            record={'schema':'koral-policy-change/1','repository':'koral-toolchain/koral-solana','issue':31,
                    'baseCommit':base,'decision':'accepted-maintainer-scope','reason':'Exact control maintenance',
                    'files':{'cli/build.gradle.kts':hashlib.sha256(b'reviewed').hexdigest()}}
            data=records/'policy-changes/koral-solana/31.json';data.parent.mkdir(parents=True);data.write_text(json.dumps(record));ref=commit(records)
            g.git(records,'update-ref','refs/remotes/origin/main',ref)
            policy={'criticalPaths':['*/build.gradle.kts']}
            body='Refs #31\nPolicy-Record: '+ref
            g.verify(product,records,base,head,body,record['repository'],policy)
            record['files']['cli/build.gradle.kts']='0'*64;data.write_text(json.dumps(record));bad=commit(records)
            with self.assertRaisesRegex(ValueError,'not merged'):
                g.verify(product,records,base,head,'Refs #31\nPolicy-Record: '+bad,record['repository'],policy)
            g.git(records,'update-ref','refs/remotes/origin/main',bad)
            with self.assertRaisesRegex(ValueError,'superseded'):
                g.verify(product,records,base,head,body,record['repository'],policy)
            with self.assertRaisesRegex(ValueError,'resulting bytes'):
                g.verify(product,records,base,head,'Refs #31\nPolicy-Record: '+bad,record['repository'],policy)
            with self.assertRaisesRegex(ValueError,'Policy-Record'):
                g.verify(product,records,base,head,'build(ci): title alone',record['repository'],policy)

if __name__=='__main__':unittest.main()
