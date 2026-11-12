# Versioning and compatibility contracts

Use Semantic Versioning. For the initial 0.x preview, patch releases preserve the declared contract; an intentional incompatible change increments the minor version and documents migration. The 0.x label does not excuse silent data corruption or hidden breaks.

| Change | Classification |
| --- | --- |
| Restore documented behavior without breaking consumers | Patch |
| Add a backward-compatible supported capability | Minor |
| Remove/rename public API or accepted source syntax | Breaking |
| Change a CLI option, artifact schema or externally used error contract incompatibly | Breaking |
| Change account discriminator, seed, size, field order or semantics | Breaking ABI |
| Raise minimum supported JVM or consumer compiler | Breaking environment requirement |
| Internal refactoring with no public effect | No automatic breaking classification |

Machine-detectable differences require human classification. A declaration/ABI dump cannot decide whether a behavioral change is safe. ABI changes must reject incompatible state safely or specify an explicit migration; never reinterpret an old same-sized account silently.

One product-version source should feed Gradle metadata, CLI identity, build manifests, archive names, tags and release notes. The current implementation contains duplicated version literals; the executable pin checker detects drift, while a future refactor should remove duplication. The initial baseline is `0.1.0-dev`; a release candidate could be `0.1.0-preview.1` after an actual version change.

Dependency/compiler/SDK changes are dedicated reviewed changes with locks and regression evidence. A test-version range is not blanket support for all future versions. Published versions and tags are immutable. Fix a bad release with a new version; do not overwrite its bytes.

See [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
