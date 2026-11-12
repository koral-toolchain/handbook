# Upstream research

Reviewed 2026-11-12. These sources inform original Koral policies; their governance, branch model, version ranges and infrastructure are not copied wholesale.

| Source | Inspected configuration | Adaptation |
| --- | --- | --- |
| [Node.js collaborator guide](https://github.com/nodejs/node/blob/main/doc/contributing/collaborator-guide.md) | Review, CI, compatibility and landing procedures | A navigable operating handbook; retain Koral's one-owner model |
| [OkHttp CI](https://github.com/lysine-dev/okhttp/blob/main/.github/workflows/build.yml) | Build JDK 21 and explicit test-runtime property across JDK 8/11/17/21 | Separate build JDK from actual runtime tests |
| [Coroutines properties](https://github.com/Kotlin/kotlinx.coroutines/blob/master/gradle.properties) and [JVM conventions](https://github.com/Kotlin/kotlinx.coroutines/blob/master/buildSrc/src/main/kotlin/kotlin-jvm-conventions.gradle.kts) | Kotlin version, toolchain and bytecode target are distinct settings | Pin implementation tooling; qualify consumer compatibility separately |
| [Spring CI](https://github.com/spring-projects/spring-framework/blob/main/.github/workflows/ci.yml) and [release verification](https://github.com/spring-projects/spring-framework/blob/main/.github/workflows/verify.yml) | Periodic runtime checks and a separate release-consumer verification project | Extra compatibility work and release verification are separate gates |
| [JUnit cross-version](https://github.com/junit-team/junit-framework/blob/main/.github/workflows/_cross-version.yml), [reproducibility](https://github.com/junit-team/junit-framework/blob/main/.github/workflows/_reproducible-build.yml), [release](https://github.com/junit-team/junit-framework/blob/main/.github/workflows/release.yml) | Separate GA/EA tests, artifact reproducibility and staged release verification | Distinguish supported gates from future-version exploration |
| [Gradle Kotlin version update](https://github.com/gradle/gradle/blob/master/.github/workflows/update-kotlin-versions.yml) | Scheduled update PRs for tested versions | Qualify upgrades explicitly instead of moving release inputs silently |
| [Kotlin contributions](https://github.com/JetBrains/kotlin/blob/master/docs/contributing.md) | Discuss language features and include corresponding tests | Larger compiler changes need prior design agreement |
| [LLVM AI policy](https://llvm.org/docs/AIToolPolicy.html) | Submitter understanding and accountability | AI assistance does not replace responsibility or owner approval |
| [Nest contributor guide](https://github.com/nestjs/nest/blob/master/CONTRIBUTING.md) and [CircleCI](https://github.com/nestjs/nest/blob/master/.circleci/config.yml) | Structured commits and separate version/verification jobs | Process inspiration, not Node-version rules for the JVM compiler |

The old `square/okhttp` repository API redirects to `lysine-dev/okhttp` at the review date; links above use that canonical repository.

Inspected revisions: OkHttp `4162e9da32f636442bc789a7576144fe5972d0a5`; coroutines `ead082131ceb45b8e4fda027c74471103c1cd09f`; Spring `817c1ad847148ec50836f62108c88660f187c152`; JUnit `c22e1f87178f145356d780b71a66bc99045a3841`; Gradle `ba196a7057b14a5a04843c7663d46b6874528f51`; Kotlin `9e4b25befe074e0412db2e2709a4aca14db4bcec`; Nest `f5a84c2ca3a76d830b733c8307ceeea82be54c18`. These are research snapshots, not Koral dependencies.

An owner-supplied private SDK was also inspected read-only for the pattern of guide -> checker -> CI job -> required branch check, and independent consumer-package testing. No company source, configuration or internal repository links are redistributed here.
