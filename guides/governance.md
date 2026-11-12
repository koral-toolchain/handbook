# Governance and review authority

@tidemark-labs is the only human maintainer, approver, merger and release authority. A contribution, star count or accepted patch does not grant write access. Repository visibility and contribution access are separate decisions.

External changes require one explicit owner approval, successful required checks and resolved blocking comments. A changed patch must be reviewed again. Bots and AI can assist; they do not provide the owner's approval. Authors must understand and verify their submissions. Repeated unverified or unrelated submissions can be closed with a reason.

The owner cannot approve their own GitHub pull request. Design review requirements with a narrowly scoped owner exception, while keeping required CI checks in a separate rule without a routine bypass. Never require a fictional second reviewer. Emergency actions must leave an incident record and pass verification before a release is published.

The organization uses GitHub Free. The owner explicitly made the compiler repository public with proprietary terms and external contributions closed. Main now requires a passing `required` Actions check, an up-to-date branch and a pull request, including for administrators. Zero additional approvals avoid requiring the sole owner to approve their own PR. Force pushes and branch deletion are disabled and blocking conversations must be resolved. These settings were checked through the GitHub API. Private repositories such as the website retain their separate visibility and plan limitations; this handbook does not authorize other visibility changes or purchases.

Reference: [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches).
