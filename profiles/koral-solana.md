# Koral Solana compiler profile

The product is an experimental Kotlin IR -> Koral checks/C backend -> public Agave SDK/LLVM -> native SBF compiler. The host JVM version is not the execution environment of the emitted Solana program.

Current modules: language, compiler, toolchain, cli. The launch scope is Counter and authority-funded System payment CPI. Do not expand it to SPL Token, PDA signing or complete DEX support merely to fill a CI matrix.

Pins and qualification targets are machine-readable in [config/koral-solana.json](../config/koral-solana.json). Existing local evidence includes unit tests, source mutation detection, invalid-source cases, account permission checks, real state/balance verification and CPI rollback. Linux x64 website workers compiled Counter and payments and passed 55/37 checks. That is not a completed cross-platform release matrix.

Performance changes compare equivalent inputs/state/permissions against independent Native Rust and Pinocchio implementations. Internal comparison provenance keeps its additional baseline and known semantic differences; public website copy remains a separate presentation decision. Never remove safety checks for a better CU number, substitute another compiler's output, or present CU as storage rent.

A changed budget needs the owner to review the before/after evidence. Correctness failures are unconditional failures; an expected cost increase for additional validation must be explained, not hidden by updating a baseline automatically.

The owner has selected proprietary, all-rights-reserved terms for original Koral code and closed external contributions during initial development. Third-party components retain their own licenses. The product source is uploaded privately to `koral-toolchain/koral-solana`. Public release, a Gradle plugin and package publishing remain separate pending work.

## Initial hosted CI evidence

Source revision `ec5b71e4c15b11a09316e58801d8abee4a433cd3` passed
[Product CI run 43163819871](https://github.com/koral-toolchain/koral-solana/actions/runs/43163819871).
This private run verifies policy, unit/build, native SBF integration, candidate
installation, compatibility and the final required gate on Ubuntu 24.04 x64.
The native integration job executes the full 53-check harness; consumer jobs
execute Counter and System payment verification from the same candidate TAR.

The tested runtime pairs are JDK 17 with Node 22 and JDK 21 with Node 24.
This does not establish all JVM/Node combinations, hosted macOS/Windows support,
the broader proposed qualification matrix, package publication or protected
private branches. The pipeline uses read-only contents permission and has no
deployment credentials or publishing job.
