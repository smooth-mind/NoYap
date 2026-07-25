# Contributing to NoYap

Thank you for helping make agent-assisted development more controlled and understandable.

## Contribution principles

A NoYap change should solve a demonstrated user problem without creating more process than it removes.

Before proposing a feature, explain:

1. the failure mode it prevents;
2. the smallest useful solution;
3. whether it belongs in the core or should remain optional;
4. how it affects context size and human review;
5. how it can be tested on a real project.

## Local checks

```bash
python scripts/noyap.py validate
python -m unittest discover -s tests -v
```

## Pull requests

Keep changes focused. Do not combine template redesign, CLI changes, and unrelated cleanup in one pull request. Include before-and-after workflow examples for behavioural changes.

## Compatibility claims

Agent products change. Claims about tool support should link to current official documentation and should distinguish automatic instruction discovery from manual compatibility.
