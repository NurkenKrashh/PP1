from datetime import datetime , timezone


line1 = input()
line2 = input()
time1 = datetime.strptime(line1, "%Y-%m-%d %H:%M:%S UTC%z")
time2 = datetime.strptime(line2, "%Y-%m-%d %H:%M:%S UTC%z")
deff = abs(time2-time1)
print(deff.seconds())