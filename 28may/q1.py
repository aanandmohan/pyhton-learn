n=int(input('enter number of student in class '))
l=[]
high=0
low=99999999999999999
count=0
for i in range(n):
    x=int(input('enter marks '))
    if x>high:
        high=x
    if x<low:
        low=x
    if x>=75:
        count+=1
    l.append(x)
print(l)
print("highest number is ",high)
print("lowest number is ",low)
print("number above than ",count)