salary=0
hra1=0
da1=0
netsal=0
while True:
    print('Menu ')
    print('1 Enter unit Consumed')
    print("2 Calculate Bill amount ")
    print("3 Apply Surcharge ")
    print("4 Display final Bill")
    print("5 exit")
    
    choice=int(input("enetr choice "))
   
    match choice:
        case 1:
            sal=int(input("Enter unit Consumed"))
            print("Units Record successfully")
            salary=sal
        case 2:
            if salary==0:
                print("please enter units consumed first ")
            else:
                if salary<100:
                    print("TOtal bill is ",salary*5)
                elif salary>100 and salary<=200:
                    t=salary%100
                    total=500+(t*7)
                    print("Total bill is ")
               
        case 3:
            if salary==0:
                print("No balance ,first depostie money ")
            else:
                print("Balnce is ",salary)
            
        case 4:
            if salary==0:
                print("No balance ,first depostie money ")
            else:
                if salary>50000:
                    up=(5/100)*salary

                    salary=up+salary
                    print("intrest ",up)
                    print("update salry is ",salary)
                else:
                    up=(3/100)*salary
                    salary=up+salary
                    print("intrest is ",up)
                    print("update salry is ",salary)

            
       
        case 5:
            print("Exist program...Thankyou")
            break
        case _:
            print("Invalid choice Please try again")