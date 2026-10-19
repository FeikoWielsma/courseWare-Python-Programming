"""A file written badly on purpose, so that ruff has something to say.

Run the linter over it and read the report :

    uv run ruff check --isolated --select A,F,I demos/14-appendix-python-tooling/02_ruff_findings.py

Preview the changes Ruff can make without changing this teaching file :

    uv run ruff check --isolated --select A,F,I --diff demos/14-appendix-python-tooling/02_ruff_findings.py

Every finding below is deliberate, so the whole file is excluded from the
repository's own ruff run in ruff.toml. Do not "fix" it here.
"""

import json  # unused import, ruff reports F401
import sys  # noqa: F401  (kept so the import block has something to sort)


def total(list):  # shadows the built-in `list`, ruff reports A002
    sum = 0  # shadows the built-in `sum`, ruff reports A001
    for i in list:
        sum = sum + i
    unused = sum * 2  # assigned and never read, ruff reports F841
    return sum


print(total([1, 2, 3]))
