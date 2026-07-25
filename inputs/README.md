# Project input attachments

Place non-secret source documents, wireframes, screenshots, or notes here when the coding agent can read local files.

Recommended organization:

```text
inputs/
├── requirements/
├── design/
├── references/
└── private/
```

`inputs/private/` is ignored by Git, but local ignore rules are not a security boundary. Never place credentials, private keys, production data, or highly sensitive personal documents in the repository.

List every reviewed source in `PROJECT_INPUT.md` so later requirements remain traceable.
