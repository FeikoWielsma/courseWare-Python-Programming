"""Replacing and splitting with a pattern."""

import re

text = "Call 020-1234567 or 010-7654321 today"

# sub replaces every match.
print(re.sub(r"\d", "x", text))
print(re.sub(r"\d{3}-\d{7}", "[redacted]", text))

# A backreference in the replacement reuses a captured group.
print(re.sub(r"(\d{3})-(\d{7})", r"\2-\1", text))

# split accepts a pattern where str.split accepts only a literal.
print(re.split(r"\s+or\s+", text))
