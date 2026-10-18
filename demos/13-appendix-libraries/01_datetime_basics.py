"""The three types the datetime module is built around."""

from datetime import date, datetime, time

photo_day = date(2026, 8, 15)
midday = time(12, 30, 0)
taken_at = datetime(2026, 8, 15, 12, 30, 0)

print(photo_day, midday, taken_at)
print("year", taken_at.year, "month", taken_at.month, "day", taken_at.day)
print("weekday", taken_at.weekday())  # Monday is 0

# The current moment comes from the class, not from a free function.
print("now is a", type(datetime.now()).__name__)
