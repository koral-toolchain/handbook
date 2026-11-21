# Enforcement map

A rule is enforced only where a concrete tool and the necessary server setting are actually enabled.

| Rule | Executable control | Current status |
| --- | --- | --- |
| Release policy v1 metadata | `tools/policy.py handbook` + rejection tests | Owner/channels/required evidence/urgent route checked; publication readiness, timing and announcements remain manual |
| Handbook/configuration consistency | `tools/policy.py handbook` | Implemented here |
| Commit shape/body/breaking marker | `tools/policy.py commit` | Wired into owner-only product CI |
| Current compiler/Gradle/CLI version agreement | `tools/policy.py versions` | Implemented; check declarations, not runtime execution |
| Missing/failed/skipped required results | `tools/policy.py gate` | Product final required gate active; release workflow pending |
| Actual JVM/Node compatibility | Product execution jobs | Linux JDK 17/Node 22 and JDK 21/Node 24 pairs passed; broader targets pending |
| Real SBF/VM regressions | Product integration job | Hosted full integration passed; see compiler profile |
| Consumer package installation | Product archive jobs | Hosted CLI extraction/install/run passed; Gradle plugin does not yet exist |
| Owner-only maintenance | CODEOWNERS, owner-only CI, protected main | Public compiler main requires PR + passing Actions gate, including admins; zero additional approvals for sole owner |
| Release approval and original-source terms | Owner-authenticated manual promotion and release gate | First GitHub prerelease published; Maven/Plugin Portal and automatic publication not configured |
| Website OIDC/SSM rollout and rollback | Separate website workflow | Implemented and live-tested |

The handbook CI checks its own policy and positive/negative cases. The compiler explicitly pins and consumes the checker with actual product tests. Other repositories still need their own integration. The public compiler now makes the gate mandatory through server settings. This does not make GitHub Free private branch protection work for other repositories.

Do not count a skipped required result as success. Keep a stable final gate name so a matrix-label change does not leave stale protection rules. Audit server rules through the API when adopting or changing them; comments in CODEOWNERS are not proof.

Some facts remain manual: code understanding, justification, correct semantic version classification and rights to contribute. This table must not relabel those as automated.

[Release policy v1](releases.md) is organization guidance. Its metadata check runs
in handbook CI, not as a universal release approval gate. The product retains its
explicitly pinned checker; new handbook rules are not silently auto-adopted by
existing product workflows. No recurring scheduler is created by the review interval.

Engineering revision 1 is defined in [engineering.md](engineering.md). The product
adopted the checker/configuration at pinned handbook commit
`e5d7ac587cb700ab094d86df5428f5e5654d4c37` through
[product PR #30](https://github.com/koral-toolchain/koral-solana/pull/30), merged as
`dc2b96a9f9d572a74a1fea074a76721a51503f2c`. All seven PR jobs succeeded in
[the verified run](https://github.com/koral-toolchain/koral-solana/actions/runs/44856504804).
The landed source tree equals the tested PR tree.

The required quality job checks pinned Kotlin/JS/Python formatting, selected
non-type-resolved detekt rules, actual bytecode dependency boundaries, repository
and local-link boundaries, actual issue/PR explanations and governed policy PR
types. Extracted-candidate jobs enforce runtime archive contents. Real controlled
formatting, long-method and wrong-checksum probes were rejected before positive
checks passed. Main protection requires the final gate including administrators.

These are concrete product controls, not an organization-wide automatic rollout.
Product value, semantic scope, justified exceptions and prose accuracy still need
owner review. No release/publication or broader platform qualification follows
from adoption. Later handbook documentation updates do not silently update the
product's pinned executable policy.
