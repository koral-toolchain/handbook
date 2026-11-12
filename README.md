# Koral Development Handbook

How Koral projects accept changes, verify compatibility, and ship releases.

This is a private organization handbook. The sole human reviewer and release authority is **@tidemark-labs**. Policies for the compiler are prepared for adoption; this handbook does not mean that the currently empty product repository already has CI or protected branches.

## Read the handbook

| Chapter | Purpose |
| --- | --- |
| [Governance](guides/governance.md) | Ownership, one-person review and enforcement limits |
| [Contributing](guides/contributing.md) | Issues, pull requests and evidence |
| [Commits](guides/commits.md) | Commit format and breaking-change records |
| [CI](guides/ci.md) | Fast checks, VM integration, artifacts and mandatory gates |
| [Compatibility](guides/compatibility.md) | Build tools versus supported consumer runtimes |
| [Versioning](guides/versioning.md) | Product/API/ABI changes and version consistency |
| [Releases](guides/releases.md) | Candidate verification, publication and recovery |
| [Security](guides/security.md) | Untrusted contributions, credentials and supply chain |
| [Enforcement map](guides/enforcement.md) | Which statements are checked, reviewed or still pending |
| [Compiler profile](profiles/koral-solana.md) | Current compiler facts and proposed qualification matrix |
| [Website profile](profiles/koral-website.md) | The independently deployed website |
| [Upstream research](references/upstream.md) | Primary sources and adaptation decisions |

## Executable policy

The handbook includes original policy checks and negative tests, not only prose:

```sh
python3 tools/policy.py handbook
python3 -m unittest discover -s tests -v
python3 tools/policy.py versions --repo /path/to/koral/utility
python3 tools/policy.py commit --message-file /path/to/message.txt
python3 tools/policy.py gate --needs-file /path/to/job-results.json
```

A successful `versions` check verifies declared pins and version consistency. It does **not** prove that a program ran on every candidate runtime. Runtime support requires actual execution evidence.

The handbook's own Actions workflow runs its checks. The reusable policy action is supplied for later installation in the product pipeline. Product unit/VM/consumer CI, package publication and GitHub merge enforcement are not installed by creating this handbook.

GitHub Free organization plans do not enforce protected branches for private repositories. Keep repositories private unless the owner explicitly changes that decision; do not buy a plan or claim that a failing check blocks every admin push. Release jobs must additionally depend on successful gates.

## Changes to rules

Change the guide, policy configuration, checker and positive/negative tests together. Do not silently relax a check to make a pull request green. Rules about correctness and rights still need human judgement; automated checks cannot establish understanding, legal ownership or absence of all vulnerabilities.
