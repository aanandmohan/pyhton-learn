n = int(input("ENTER SIZE OF LIST = "))
a = []

for i in range(n):
    a.append(int(input()))
k = int(int(input("ENTER k = ")))
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==k:
            print(f"({a[i]},{a[j]})")
            count+=1
print(count)