from datetime import datetime
from zoneinfo import ZoneInfo

almaty = datetime.now(ZoneInfo("Asia/Almaty"))
london = datetime.now(ZoneInfo("Europe/London"))
newyork = datetime.now(ZoneInfo("America/New_York"))

print("Almaty:", almaty)
print("London:", london)
print("New York:", newyork)