# Build pins and compatibility qualification

Four different versions must not be conflated:

1. The Kotlin compiler/plugin used to build or implement Koral.
2. The JDK running Gradle or the installed Koral CLI.
3. The JVM bytecode target of the host-side JAR.
4. The Solana SBF target of the emitted native program.

Node.js is a dependency of the VM testing tools, not the runtime of the compiler itself.

## Current facts and planned targets

| Axis | Current pin/evidence | Proposed required qualification | Additional exploration |
| --- | --- | --- | --- |
| Embedded Kotlin | 2.2.21, coupled to the IR plugin | Keep compiler and plugin equal | One explicitly selected next compiler version |
| Build JDK / bytecode | Toolchain and target 17 | Build using the pinned toolchain | Upgrade only with a reviewed compatibility change |
| CLI host runtime | JDK 17 locally exercised | JDK 17 and 21 execution | JDK 25 canary |
| Gradle | Wrapper 8.14.6 plus checksum | Wrapper build and archive integrity | Compatible newer wrapper in a separate PR |
| Test Node.js | 22.22.3 observed; package minimum >=22.12 | Node 22 and 24 qualification | Node 26 canary |
| Solana toolchain | Agave 3.1.10 / tools 1.52 / SBFv0 | Pinned reference for correctness and CU | Explicit isolated upgrade investigation |
| Local VM | LiteSVM 1.6.1 | Identical pinned fixture semantics | Independent update PR |
| OS/architecture | Full local macOS arm64 checks; Linux x64 example verification | Full Linux x64 suite and macOS arm64 release smoke | Other hosts after actual qualification |

This table is a target plan, not a claim that every row is already supported. No native Windows or WSL support is promised.

## Avoid a fake matrix

Changing `JAVA_HOME` to 21 while Gradle tests still launch the 17 toolchain does not prove JDK 21 runtime support. Execute the installed CLI with the selected Java executable and record `java -version`. Node matrix jobs must actually use and record that Node runtime. Reusing an identical compiled ELF to test another VM-host Node version is valid; relabeling the same Node execution is not.

The Kotlin IR plugin and embedded compiler currently both pin 2.2.21. Adding a label for Kotlin 2.4 does not make it compatible. A compiler-version matrix needs real dependency selection, plugin recompilation and regression execution. Do not mix this with the future consumer project's Kotlin/Gradle matrix.

Gradle 8.14.6 must not be run under JDK 25 merely because it is a newer LTS; Gradle's documented JDK 25 runtime support starts at 9.1.0. A JDK 25 CLI canary can run an artifact built under the qualified build JDK, or use a separately qualified wrapper.

Candidate failures do not block an already supported release solely because a future unsupported version failed. Supported-target failures always block release. Promotion requires the full relevant suite, consumer tests, a support-table change and owner approval. Resolve candidates to exact versions before claiming support; do not use a moving `latest` as release provenance.

Sources: [Kotlin compiler plugin stability](https://kotlinlang.org/docs/custom-compiler-plugins.html), [Kotlin toolchains](https://kotlinlang.org/docs/gradle-configure-project.html), [Gradle compatibility](https://docs.gradle.org/current/userguide/compatibility.html).
