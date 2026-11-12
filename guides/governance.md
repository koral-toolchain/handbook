# Governance and review authority

@tidemark-labs is the only human maintainer, approver, merger and release authority. A contribution, star count or accepted patch does not grant write access. Repository visibility and contribution access are separate decisions.

External changes require one explicit owner approval, successful required checks and resolved blocking comments. A changed patch must be reviewed again. Bots and AI can assist; they do not provide the owner's approval. Authors must understand and verify their submissions. Repeated unverified or unrelated submissions can be closed with a reason.

The owner cannot approve their own GitHub pull request. Design review requirements with a narrowly scoped owner exception, while keeping required CI checks in a separate rule without a routine bypass. Never require a fictional second reviewer. Emergency actions must leave an incident record and pass verification before a release is published.

Currently the organization uses GitHub Free and the product repository is private. Mandatory private branch protection needs an eligible paid plan, or an explicitly authorized public repository. The owner has made this handbook public. Product repositories retain their separately chosen visibility; this handbook does not authorize other visibility changes or plan purchases. Documentation, failed CI and server-enforced merge protection are three different things.

Reference: [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches).
