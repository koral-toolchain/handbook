# Enforcement map

A rule is enforced only where a concrete tool and the necessary server setting are actually enabled.

| Rule | Executable control | Current status |
| --- | --- | --- |
| Handbook/configuration consistency | `tools/policy.py handbook` | Implemented here |
| Commit shape/body/breaking marker | `tools/policy.py commit` | Implemented; product CI wiring pending |
| Current compiler/Gradle/CLI version agreement | `tools/policy.py versions` | Implemented; check declarations, not runtime execution |
| Missing/failed/skipped required results | `tools/policy.py gate` | Implemented; product release workflow wiring pending |
| Actual JVM/Node compatibility | Product execution matrix | Proposed qualification; no matrix has run here |
| Real SBF/VM regressions | Existing product tests, future required CI jobs | Local evidence exists; product Actions pending |
| Consumer package installation | Product archive/TestKit jobs | CLI test design; plugin does not yet exist |
| Owner-only review | CODEOWNERS plus protected rules | Owner decision; private Free enforcement limitation |
| Public namespace/license and release approval | Owner plus release workflow | Publication not configured |
| Website OIDC/SSM rollout and rollback | Separate website workflow | Implemented and live-tested |

The handbook CI checks its own policy and positive/negative cases. It cannot silently install the product pipeline or make GitHub Free private branch protection work. A consumer must explicitly pin and wire the policy action, add actual tests, and make the gate mandatory where supported.

Do not count a skipped required result as success. Keep a stable final gate name so a matrix-label change does not leave stale protection rules. Audit server rules through the API when adopting or changing them; comments in CODEOWNERS are not proof.

Some facts remain manual: code understanding, justification, correct semantic version classification and rights to contribute. This table must not relabel those as automated.
