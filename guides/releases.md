# Release policy v1

Status: adopted organization policy. Start with this small policy, use it for the
next release, and improve it through reviewed changes. It sets no automatic
publication schedule. Existing verification requirements below remain in force.

## When to publish

Record user-visible changes in each product's Unreleased changelog and update
usage documentation as changes land. A merged PR is not a published release.
Group related changes around a useful user outcome, rather than a count of PRs.

Review release readiness roughly every two weeks. This is an owner reminder,
not a scheduler or a deadline: skip publication if there is no useful, verified
update. Do not hold an urgent correctness/security or installation fix for the
regular review. Urgent releases still need the relevant evidence and owner
approval; urgency does not turn a failed required check into success.

## Preview and stable

- **Preview:** an explicitly marked prerelease version and GitHub prerelease.
  State supported examples, known limitations and compatibility changes.
- **Stable:** an intentional owner decision about a documented, tested support
  contract, with a non-prerelease version. Passing CI or removing a suffix alone
  does not qualify a product as stable.

Apply [versioning rules](versioning.md) to API, ABI, CLI and environment changes.
Initial 0.x changes still need explicit compatibility and migration notes.
Policy revision v1 is independent of each product's version. It does not bump
any product, create a tag or change usage rights.

## Minimum publication decision

Before the owner promotes a candidate, confirm all of the following:

| Condition | Current enforcement |
| --- | --- |
| Required CI succeeds for the selected source | Product-specific CI and server protection where configured |
| Actual candidate installs and executes supported examples | Product CI evidence, checked by the owner against the selected artifact |
| Relevant behavioral regressions pass | Product CI; the product checklist defines the actual scenarios |
| Changelog, usage docs, version and compatibility notes agree | Owner review; existing version-pin checks cover declarations only |
| Exact asset identity, notices and exclusions are verified | Owner review/manual release checks; no universal publishing workflow |
| @tidemark-labs explicitly approves this candidate and version | Manual owner-initiated promotion; merging is not release approval |

Use the [compiler checklist](https://github.com/koral-toolchain/koral-solana/blob/main/docs/RELEASING.md)
for Koral Solana. Future products add their own checklist rather than inheriting
Solana-specific tests blindly. Current metadata is in
[config/release-policy.json](../config/release-policy.json). Handbook CI checks
that metadata's consistency; it does not certify a release candidate or publish it.

## Release notes and announcements

Every published product version gets a GitHub Release with changes, installation,
known limitations and compatibility notes. This is the complete release record.
A homepage Updates article and X announcement are selective: use them when a
released group of changes has a clear user benefit and a runnable example.
Small fixes may remain in release notes without a dedicated promotional post.
Development posts must say source-only/unreleased when the download lacks a feature.

The owner decides whether an urgent issue needs an immediate user advisory.
For a faulty release, describe the impact and a known-good version, then publish
a corrected version. Do not move tags or replace published asset bytes in place.
For a suspected security issue, avoid disclosing exploit details before a safe
fix and appropriate advisory are ready; follow [security guidance](security.md).

After the next actual release, review friction and amend this policy through an
issue/PR. Larger automation, publication registries and additional maintainers
can be added when needed; v1 does not claim they already exist.

# Candidate verification and website deployment

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
