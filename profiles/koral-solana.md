# Koral Solana compiler profile

The product is an experimental Kotlin IR -> Koral checks/C backend -> public Agave SDK/LLVM -> native SBF compiler. The host JVM version is not the execution environment of the emitted Solana program.

Current modules: language, compiler, toolchain, cli. The launch scope is Counter and authority-funded System payment CPI. Do not expand it to SPL Token, PDA signing or complete DEX support merely to fill a CI matrix.

Pins and qualification targets are machine-readable in [config/koral-solana.json](../config/koral-solana.json). Existing local evidence includes unit tests, source mutation detection, invalid-source cases, account permission checks, real state/balance verification and CPI rollback. Linux x64 website workers compiled Counter and payments and passed 55/37 checks. That is not a completed cross-platform release matrix.

Performance changes compare equivalent inputs/state/permissions against independent Native Rust and Pinocchio implementations. Internal comparison provenance keeps its additional baseline and known semantic differences; public website copy remains a separate presentation decision. Never remove safety checks for a better CU number, substitute another compiler's output, or present CU as storage rent.

A changed budget needs the owner to review the before/after evidence. Correctness failures are unconditional failures; an expected cost increase for additional validation must be explained, not hidden by updating a baseline automatically.

The owner has selected proprietary, all-rights-reserved terms for original Koral code and closed external contributions during initial development. Third-party components retain their own licenses. The product repository remains private and empty; product source now contains CI definitions pending its first upload and hosted run. Public release, a Gradle plugin and package publishing remain separate pending work.
