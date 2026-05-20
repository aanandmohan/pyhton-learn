emp=input("enter employ id ")
flag=1
if emp.startswith("EMP"):
    for i in range(3,len(emp)):
        if emp[i]>='0' and emp[i]<='9':
            flag=0
        else:
            print("not valid ")
            break
    else:
        print("valid ")
    
else:
    print("nott valid ")

