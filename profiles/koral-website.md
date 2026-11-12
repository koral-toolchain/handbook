# Koral website profile

Source: private `koral-toolchain/koral-website`. Live site: https://koral.tools . Product implementation is separate.

The current workflow validates the adapter and deterministic release packaging, builds static documentation, obtains a main-only OIDC role, uploads an encrypted private archive and invokes one dedicated SSM document on the designated Seoul EC2 host. It does not store a long-lived AWS or SSH key in GitHub Secrets.

The role cannot terminate instances or run an arbitrary SSM shell document. The host reads only its release prefix in addition to SSM management permissions. Rollout verifies archive identity and health, atomically changes the current release, and restores the prior version on failure. A controlled unhealthy deployment was rejected and the previous version recovered. A second static-only deployment was verified without restarting the adapter.

Treat this as an implemented product-specific control, not a template that grants every Koral repository deployment rights. Compiler updates need a separately supplied, verified image; arbitrary contributed Kotlin is not accepted by the demonstration API.

The human maintainer is tidemark-labs. Repository access is private; the website itself is public. Certificate renewal is automated. Domain registration renewal is a separate account setting and is currently disabled for the one-year registration.
