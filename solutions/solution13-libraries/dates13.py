"""Solution to Exercise 13, step 1 : datetime."""

from datetime import date, datetime


def days_until(target: date) -> int:
    """Return the number of days between today and a target date."""
    return (target - date.today()).days


new_year = date(date.today().year + 1, 1, 1)
print(f"days until New Year : {days_until(new_year)}")

today = date.today()
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A %d %B %Y"))
print(today.isoformat())

parsed = datetime.strptime("24-12-2026 18:00", "%d-%m-%Y %H:%M")
print(f"{parsed} falls on a {parsed.strftime('%A')}")
