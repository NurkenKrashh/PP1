from datetime import datetime
now = datetime.now()
time = now.strftime("%d-%m-%Y")
print(time) 


from datetime import datetime
day = "27-02-2026"
time = datetime.strptime(day,"%d-%m-%Y")
print(time)