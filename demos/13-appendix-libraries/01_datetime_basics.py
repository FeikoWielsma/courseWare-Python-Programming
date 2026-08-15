"""The three types the datetime module is built around."""

from datetime import date, datetime, time

today = date(2026, 8, 15)
midday = time(12, 30, 0)
launch = datetime(2026, 8, 15, 12, 30, 0)

print(today, midday, launch)
print("year", launch.year, "month", launch.month, "day", launch.day)
print("weekday", launch.weekday())  # Monday is 0

# The current moment comes from the class, not from a free function.
print("now is a", type(datetime.now()).__name__)
