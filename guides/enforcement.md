# Enforcement map

A rule is enforced only where a concrete tool and the necessary server setting are actually enabled.

| Rule | Executable control | Current status |
| --- | --- | --- |
| Handbook/configuration consistency | `tools/policy.py handbook` | Implemented here |
| Commit shape/body/breaking marker | `tools/policy.py commit` | Wired into owner-only product CI |
| Current compiler/Gradle/CLI version agreement | `tools/policy.py versions` | Implemented; check declarations, not runtime execution |
| Missing/failed/skipped required results | `tools/policy.py gate` | Product final required gate active; release workflow pending |
| Actual JVM/Node compatibility | Product execution jobs | Linux JDK 17/Node 22 and JDK 21/Node 24 pairs passed; broader targets pending |
| Real SBF/VM regressions | Product integration job | Hosted full integration passed; see compiler profile |
| Consumer package installation | Product archive jobs | Hosted CLI extraction/install/run passed; Gradle plugin does not yet exist |
| Owner-only maintenance | CODEOWNERS, owner-only CI, protected main | Public compiler main requires PR + passing Actions gate, including admins; zero additional approvals for sole owner |
| Public namespace/license and release approval | Owner plus release workflow | Publication not configured |
| Website OIDC/SSM rollout and rollback | Separate website workflow | Implemented and live-tested |

The handbook CI checks its own policy and positive/negative cases. The compiler explicitly pins and consumes the checker with actual product tests. Other repositories still need their own integration. The public compiler now makes the gate mandatory through server settings. This does not make GitHub Free private branch protection work for other repositories.

Do not count a skipped required result as success. Keep a stable final gate name so a matrix-label change does not leave stale protection rules. Audit server rules through the API when adopting or changing them; comments in CODEOWNERS are not proof.

Some facts remain manual: code understanding, justification, correct semantic version classification and rights to contribute. This table must not relabel those as automated.
