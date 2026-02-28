from datetime import datetime, timedelta

now = datetime.now()

print("Current Date & Time:", now)
print("Year:", now.year)

formatted = now.strftime("%d/%m/%Y")
print("Formatted:", formatted)

next_week = now + timedelta(days=7)
print("Next Week:", next_week)