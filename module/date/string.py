from datetime import datetime,timedelta
'''str=input("enter date ")
dt=datetime.strptime(str,"%d-%m-%y")
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)'''

dob1=datetime(2026,2,10)
dob2=datetime(2024,4,20)
d=dob1-dob2
print(d)
print(d.seconds)