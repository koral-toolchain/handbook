# Commit messages

The final landed commit and PR title use:

```text
<type>(<scope>): <subject>

<body explaining the reason and verification>
```

Types: `feat`, `fix`, `perf`, `refactor`, `test`, `docs`, `build`, `ci`, `chore`, `revert`.

Product scopes are declared in [the policy configuration](../config/koral-solana.json). Omit the scope for a repository-wide change. Use an English, descriptive subject, no final period and at most 72 characters. Avoid generic subjects such as `update` or `fix stuff`. Do not infer correctness from formatting alone.

`feat`, `fix` and `perf` require a body. Breaking changes require both `!` in the header and a `BREAKING CHANGE:` paragraph describing the consumer impact. Examples:

```text
fix(runtime): reject read-only payment recipients

A recipient without writable permission could reach the transfer path.
Reject it before CPI and verify the unchanged balances on failure.
```

```text
feat(language)!: version the stored account layout

BREAKING CHANGE: earlier account layouts require an explicit migration.
```

Initial product policy uses squash merging, so the final squash title is checked and the final message retains the reason and relevant human attribution. Feature-branch fixup commits need not become permanent history. A release is not automatically versioned solely from commit type; the actual public contract is reviewed too.

See [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
