# Release and deployment rules

Product CI, package publication and website deployment are separate pipelines.

## Product release gate

A main-branch commit can produce development artifacts. It does not automatically publish to Maven Central, the Plugin Portal or a blockchain. Only @tidemark-labs initiates a release, using a selected version and exact reviewed commit.

Before publication:

1. The full required result gate passes on the selected commit, including supported runtime checks, native integration and consumer artifact installation.
2. Version, tag, manifest and changelog agree; public/API/ABI changes are classified.
3. The own-source license and third-party notices are selected and checked. Publication coordinates, namespace and plugin ID are actually owned.
4. Archive contents exclude credentials, account files, wallet keypairs, private studio history, caches and unrelated experiments.
5. Freshly installed artifacts pass on the minimum supported host; checksums and build provenance identify source commit, dependencies and toolchain.
6. The owner confirms promotion of that verified candidate. CI never replaces it with a newly rebuilt unverified payload after approval.

Use a preview channel first. Verify actual downloadable/installable bytes before promoting a stable version. Package registries are not atomically reversible across multiple modules; a partial publication is an incident, not permission to overwrite an existing version. Keep promotion and recovery steps documented.

The Gradle plugin and Maven/Plugin Portal publication are not implemented yet. A private source repository or a passing handbook check is not a published product.

## Website deployment

The separate private website repository already deploys main via scoped OIDC, a private S3 archive and a fixed SSM command. It switches release directories, checks health and restores the previous version on failure. Static-only edits do not rebuild the compiler or restart the adapter. That mechanism is described in [the website profile](../profiles/koral-website.md).

Updating the compiler in the website requires a reviewed immutable image identity and real example verification. Product PRs must not receive website deployment rights. Do not copy a permanent AWS key to GitHub, or run public PR code on the production host.

## What a release records

Record the tested commit, version, supported environments, checksums, known limitations, compatibility changes and recovery instructions. Optional provenance/SBOM tooling must be chosen and verified before claiming it exists. No release implies a security audit, general Kotlin support, mainnet deployment or financial activity.
