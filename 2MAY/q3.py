r=int(input("enter row "))
c=int(input("enter column "))
m=[]
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input("enter elemnt ")))
    m.append(row)

print(m)

while True:
    print("1find armstrong number row wise ")
    print("2 count palindrom number column  wise ")
    print("3 find avergae row wise ")
    print("4 exit ")
    choice=int(input("enter choice "))
    match choice:
        case 1:
            for i in range(r):
                count=0
                for j in range(c):
                    k=m[i][j]
                    z=k
                    t=len(str(k))
                    sum=0
                    while k>0:
                        s=k%10
                        sum+=s**t
                        k=k//10
                    if sum==z:
                        count+=1
                print(f"the count of armstrong number {i+1} row is ",count)

        case 2:
            for i in range(c):
                count=0
                for j in range(r):
                    k=m[j][i]
                    temp=k
                    rev=0
                    while k>0:
                        s=k%10
                        rev=rev*10 +s
                        k=k//10
                    if rev==temp:
                        count+=1
                print(f"number of palindrom in {i+1} ",count)
        case 3:
            for i in range(r):
                sum=0
                for j in range(c):
                    sum+=m[i][j]
                print(f"the average of{i+1} row is  ",sum/c)
        case 4:
            print("process exit ")
            break





