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
    print(" 1 count prime number ")
    print(" 2 count perfect Number column wise ")
    print("3 diplay Row-wise ")
    print("4 exit ")
    choice=int(input('enter choice '))
    match choice:
        case 1:
            
            for i in range(r):
                count=0
                for j in range(c):
                    if m[i][j]>1:
                        for k in range(2,m[i][j]//2+1):
                            if m[i][j]%k==0:
                                break
                        else:
                            count+=1   
                print(f"count of prime number in {i+1} ",count)
                print()
        case 2:
            for i in range(c):
                
                count=0
                for j in range(r):
                    k=m[j][i]
                    t=0
                    for l in range(1,k):
                        if k%l==0:
                            t+=l
                    if t==k:
                        count+=1
                print(f"the number of perfect number in {i+1}",count)
        case 3:
            for i in range(r):
                sum=0
                for j in range(c):
                    sum+=m[i][j]
                print(f"the row is sum is {i+1} ",sum)
        case 4:
            print("process exit ")
            break


                            



            
                        

    

    