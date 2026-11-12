# Security and supply chain

Accept untrusted submissions as data until reviewed. In particular inspect workflow changes, editor auto-run tasks, binary additions, wrapper changes and dependency scripts before checking out or executing them on a privileged machine. Gradle's wrapper JAR is an explicitly reviewed infrastructure artifact, not permission to commit arbitrary binaries.

Use `pull_request` with minimal read access for untrusted tests. Do not check out or execute an untrusted head in `pull_request_target`. A future metadata-only guard may use the base workflow and REST data without running contributed code; it needs separate review.

Checks and release jobs use the least permissions they need. Pin dependency locks, action commits, SDK archives and checksums. Keep privileged release credentials out of verification jobs and isolate their caches. A policy change must not quietly delete a required check or broaden an OIDC subject to other repositories or branches.

Do not put secrets, account files or signing keys in Git, archives, logs or test fixtures. Deterministic local VM test identities are not funded production wallets. CI must not submit a live transaction or spend funds.

Security reports need a private owner-controlled route, configured before public contribution is invited. Do not invent a security mailbox, response SLA or bounty. Proven vulnerabilities are patched and disclosed through an explicit owner-led process. AI review and a clean static scan are useful evidence, not a security audit.
