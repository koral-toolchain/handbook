# Controlled engineering

Status: policy adopted in this handbook; Koral Solana adopted it through product PR #30. Each additional product must explicitly pin and implement it. This document alone does not enable a product gate. The authoritative identifiers and references are in [engineering.json](../config/engineering.json).

Every non-trivial change starts with an issue describing the user outcome, acceptance criteria and exclusions. A PR links the actual issue and records scope, acceptance, exclusions, validation and compatibility. A checker can verify structure and issue identity; only the owner decides whether a feature belongs in the product. Closed external contributions and the sole maintainer remain unchanged.

## Reference and exception rules

Use the official Kotlin conventions followed by kotlinx.coroutines. Pin tools and reference revisions. ktlint's documented default profile adds mechanical decisions where the guide is silent; do not confuse it with the identical IntelliJ profile. Kotlin compiler sources and Gradle scripts use it; the restricted contract DSL, embedded generated C, published artifacts and third-party texts have distinct compatibility requirements.

Use selected detekt rules with their versioned default thresholds. At first adoption, enable complex conditions, cyclomatic complexity, long methods/parameter lists, deep nesting, large classes, naming and package/file agreement. Pure single-when dispatch is handled as in detekt's own configuration. No baseline silently accepts existing findings. Compiler intrinsic stubs intentionally do not execute their parameters; protocol tags are not arbitrary application constants. Non-type-resolved analysis does not establish type-resolved coverage.

Architectural tests check the product's declared module and package boundaries. These are Koral decisions, using a referenced testing tool; they are not rules invented by an upstream library. A semantic decision such as a cohesive class cannot be certified from line counts.

Every exception needs the affected rule, exact scope, reason and verification. New suppressions, excluded paths, baseline files and softened rules require an explicit policy-change issue/PR. Keep policy changes separate from feature work. Never add broad exclusions merely to pass CI.

## Verification and delivery

Formatting, static analysis, architecture, repository/documentation and distribution checks join the existing real SBF and installed-consumer jobs. Missing, skipped, cancelled or failed required results fail the final gate. Local commands and hosted CI must run the same checks. Negative tests must demonstrate rejection of malformed requests, forbidden dependencies/files and stale or incomplete results.

Dependency locks and checksum metadata are reviewed inputs, not proof that downloaded code is trustworthy. Generated release candidates must contain only declared runtime files and notices; internal tools, keys, caches, websites and SDK binaries are excluded. Compile and execute the extracted archive outside the checkout.

Documentation changes accompany behavior/CLI/ABI/environment changes. Mechanical checks validate links, declarations and executable examples; owner review validates meaning and support claims. Never claim a release, audit or platform based on unexecuted checks.

Main requires a PR and the final required gate, applying to administrators as well. The owner remains the sole human reviewer. Policy updates do not publish the product or deploy a blockchain program. Release promotion follows [the separate release policy](releases.md).
