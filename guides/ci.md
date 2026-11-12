# CI and required gates

The pipeline checks the product that a developer receives, not only its source tree.

## Layers

| Layer | Work | When |
| --- | --- | --- |
| Policy | Commit/PR format, pins, version agreement, dependency locks | Every product PR |
| Fast validation | Build, focused unit tests, static checks | Every product PR, including drafts |
| Native integration | Real SBF compilation, positive and negative VM behavior | Ready code PRs and main |
| Consumer installation | Extract CLI into an empty directory; use only declared runtime inputs | Ready packaging/core PRs and releases |
| Compatibility | Actual installed CLI/runtime execution on qualified targets | Ready PRs; full release matrix |
| Performance | Correctness-equivalent CU comparison with fixed provenance | Affected compiler/runtime PRs and releases |
| Release | Complete matrix, distribution, version and publication checks | Owner-requested release |

Product job implementations are pending adoption. [The compiler profile](../profiles/koral-solana.md) separates known local evidence from these targets.

## Failure means failure

A final required gate examines every expected job. `failure`, `cancelled`, `skipped` and missing results fail it. Do not hide errors with `|| true`, ignore an exit status, remove tests, silently lower a budget or make a required matrix job experimental. Conditional docs/draft paths need an explicit policy; they must not make a ready code PR appear fully validated.

The executable `gate` command implements the result check. `--stage release` additionally requires benchmarks, artifact integrity and release authorization; it cannot be satisfied by only the PR job set. The authorization job must verify the trusted GitHub actor/event/ref; a contributor-supplied JSON statement is not approval. Workflow publication jobs must use `needs` plus this gate. GitHub required-check settings must then make its status mandatory where the plan supports enforcement. Renaming a check or changing a required matrix must update the server rules and policy in the same change.

## Test what is shipped

Extract the CLI ZIP/TAR outside the repository. Use a fresh working directory and dependency cache. Check `doctor`, source checking, compilation, emitted C/ABI/hash metadata and local VM behavior. Fail when a consumer needs hidden studio directories, an undeclared dependency, or a different registry artifact substituted for the candidate.

Once a Gradle plugin exists, publish its candidate to a temporary local Maven repository and run a separate consumer build using only those coordinates. Source project substitution is not package verification. Before that plugin exists this test is explicitly not applicable, not a fake green result.

## Isolation and cost

Use disposable hosted runners for untrusted code; never the production EC2 host. Fork PRs have read-only checkout access, no deployment secrets, no publishing permission and no cloud OIDC. Review workflow changes before authorizing all outside contributors' runs. Pin third-party actions to full commit SHAs. Untrusted jobs do not populate caches consumed by privileged release jobs.

Cancel superseded PR verification to control cost. Do not cancel a package publication halfway through. Parallel matrix failures should remain visible; `fail-fast: false` is not permission to ignore a failed job. Run the broad future-version matrix on a schedule rather than rebuilding every combination on every draft.
