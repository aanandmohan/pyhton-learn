from datetime import datetime
# today=date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)


now=datetime.now()
f=now.strftime("%Y-%m-%d")
print(f)
f=now.strftime("%y-%B-%d")
f=now.strftime("%Y-%B-%H")
print(f)
t=now.strftime("%H-%M-%S%p")

k=now.strftime("%A")
print(k)
k=now.strftime("%a")
print(k)
k=now.strftime("%j")
print(k)

print(t)
print(now)
print(now.year)
print(now.month)