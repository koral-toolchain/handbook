# Issues and pull requests

Use one problem per pull request. Discuss language features, public API/ABI changes, new dependencies and structural rewrites before implementing them. Small focused bug fixes and documentation corrections can start as pull requests.

A code PR explains the trigger, previous behavior, intended behavior, implementation choice and compatibility impact. Bug fixes include a regression that fails without the fix and passes with it. Compiler/runtime changes include relevant actual SBF and local VM verification, not only a Kotlin parser or mock test.

Required evidence depends on the change:

| Change | Evidence |
| --- | --- |
| Parser/frontend or diagnostic | Accepted/rejected source and source-position diagnostics |
| State/runtime/CPI | State bytes, permissions, balances, failures and rollback |
| Public API or ABI | Contract diff, migration or explicit incompatibility, version impact |
| Performance | Fixed-toolchain before/after comparison and correctness-equivalent inputs |
| Dependencies/build | Lockfiles, artifact installation and supply-chain review |
| Documentation | Accurate claims, working commands/links; no invented support |

PR descriptions distinguish executed checks from skipped checks. A checked box is a factual statement. Do not submit unreviewed AI output or outsource understanding to the maintainer. Disclose material AI assistance and take responsibility for the resulting code.

The initial product branch model is one integration branch, `main`, with immutable release tags. It is intentionally smaller than a large organization's multi-branch release train. A ready PR must satisfy the full required gate; a draft's fast checks never authorize a release.

Public behavior changes need an Unreleased changelog entry. Documentation-only edits do not need artificial unit tests. New behavior and regressions require meaningful tests. Preserve legitimate human attribution; an AI tool is not a human co-author.
