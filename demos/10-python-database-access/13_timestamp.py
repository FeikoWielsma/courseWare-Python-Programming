from datetime import datetime

taken_at = datetime(2026, 10, 17, 10, 8, 15)
print(taken_at.isoformat(timespec="seconds"))

recorded_at = datetime.now().isoformat(timespec="seconds")
