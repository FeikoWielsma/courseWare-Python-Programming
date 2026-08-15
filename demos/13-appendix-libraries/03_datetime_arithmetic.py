"""Differences between dates, and dates shifted by a duration."""

from datetime import date, timedelta

start = date(2026, 8, 15)
end = date(2026, 12, 24)

# Subtracting two dates gives a timedelta.
span = end - start
print("days between:", span.days)

# Adding a timedelta to a date gives another date.
print("a week later:", start + timedelta(weeks=1))
print("100 days later:", start + timedelta(days=100))
print("yesterday:", start - timedelta(days=1))
