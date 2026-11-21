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
and local-link boundaries, actual issue/PR explanations and the revision-1 policy PR title rule (superseded by the revision-2 scope record). Extracted-candidate jobs enforce runtime archive contents. Real controlled
formatting, long-method and wrong-checksum probes were rejected before positive
checks passed. Main protection requires the final gate including administrators.

These are concrete product controls, not an organization-wide automatic rollout.
Product value, semantic scope, justified exceptions and prose accuracy still need
owner review. No release/publication or broader platform qualification follows
from adoption. Later handbook documentation updates do not silently update the
product's pinned executable policy.

## Control-hardening follow-up

The seven successful PR checks above are not a claim that every later main run
succeeded. Post-merge run 44857096234 failed during dependency resolution before a
negative probe could run. Product issue #31 tracks positive preparation/offline
probe separation, base-trusted critical scope and exact runtimeClasspath archive
identity. Revision 2 adoption requires its own PR and post-merge evidence; a merged
scope record alone is not release readiness or independent approval evidence.

## Engineering revision 2 adoption

[Product PR #32](https://github.com/koral-toolchain/koral-solana/pull/32) merged as
`83a43718a04d10e4097e4b9d4b9460253ca98eae` after all seven jobs succeeded in
[PR run 44862799177](https://github.com/koral-toolchain/koral-solana/actions/runs/44862799177).
Tested and landed trees both equal `efbf6e6d3882aac73fc2e201b416b93e13158c43`.
[Post-merge main run 44863330571](https://github.com/koral-toolchain/koral-solana/actions/runs/44863330571) finished successfully. Its first quality attempt exhausted bounded retries on Maven Central HTTP 429 before probes; one failed-jobs rerun of the same commit passed quality and the final gate. No source, rule, checksum or lock change was used for recovery. The original failure remains in attempt 1.

The executable checker is pinned independently at
`7ec0ab17c05940a676e91cc71037b349b4532629`; the separately merged data record is
`19576a616644d67ddf53c02c695f33ba0ac6b3f7`, scoped to product issue #31, exact base
`dc2b96a9f9d572a74a1fea074a76721a51503f2c` and sixteen critical-file digests.
The guard rejects stale/unmerged scopes and changed file bytes. Manual verification
is main-only and PRs target protected main. Positive dependency preparation precedes
offline formatting/long-method/checksum probes, followed by restored positive checks.
Extracted archives must match a separate Gradle runtimeClasspath manifest in exact
JAR names and SHA-256 values; missing, injected, duplicated or replaced JARs fail.

These checks do not prove independent human intent or upstream authenticity.
The owner still reviews scope and controls workflow administration. New product
capabilities are paused by owner direction while procedural controls are hardened.
No release assets, language capability or website deployment changed.

Manifest identity checks inspect main Kotlin sources in both the CLI and shared
pipeline module. Exactly one explicit manifest compiler version must agree with
Gradle, CLI identity and the pinned product version. This supports moving the
writer without accepting duplicate or drifting declarations. Dedicated tests cover
the legacy CLI writer, pipeline writer, duplicate writer and mismatched version.
Product adoption requires an explicit checker-pin update and governed scope record.

## Shared compiler pipeline adoption

[Product PR #34](https://github.com/koral-toolchain/koral-solana/pull/34) merged as
`13f1fb2cc63dd8116ae06a7666213ecd2b615cdb` after all seven jobs succeeded in
[PR run 44876004872](https://github.com/koral-toolchain/koral-solana/actions/runs/44876004872).
Tested and landed trees both equal `4a6f36026e1d9c0dc1a87c21ec98e42a858c94db`.
[Post-merge main verification](https://github.com/koral-toolchain/koral-solana/actions/runs/44876577523) also completed successfully, with all seven jobs passing.

The product uses responsibility names kotlin, ir, validation, target.c and abi,
with pipeline as the shared JVM/CLI compilation coordinator. Its production
bytecode must follow an explicit nine-role dependency table, and every production
class must have exactly one role. Real compiled Java fixtures demonstrate that
all 56 forbidden directions are rejected. This replaces the earlier incomplete
manual direction list.

Extracted candidates compile a consumer driver against installed JARs and call the
JVM pipeline without CLI handlers. Library/CLI C, ABI and SBF must match, and failed
source must invalidate old success artifacts. Four maintained contracts also had
identical generated C/ABI/SBF before and after on the same local SDK; that is not
a new gas/CU benchmark or a general compiler-correctness proof.

The adopted version checker is pinned at
`f0d5a89842e9a2ebac2a99ad2106058a31b65a6b`; its separately merged issue #33 scope
record is `c37af9c62778cc44eeb11706bb00250700f35151` and binds ten critical files
to base `83a43718a04d10e4097e4b9d4b9460253ca98eae`. Initial PR checks correctly
blocked a CLI-only writer assumption and then a stale scope; checker tests and an
updated explicit scope resolved them. Versions and unique-identity checks were not
relaxed. Later documentation does not change either pinned identity.

Internal JVM packages changed and implementation-level callers must update their
imports. Existing contract semantics, wire ABI and runtime C remain unchanged.
The public 0.3.0-preview.1 assets/tag were not replaced. No JNI layer, new compiler
process boundary, language capability, website deployment or release follows from
this refactor. Role boundaries are product-specific decisions, not a ban on all
necessary cross-component calls or an organization-wide automatic integration.
