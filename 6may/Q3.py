salary=0

while True:
    print('Menu ')
    print('1 Deposite money')
    print("2 Withdrwal money ")
    print("3 Check Balnce ")
    print("4 Apply Intrest")
    print("5 exit")
    
    choice=int(input("enetr choice "))
   
    match choice:
        case 1:
            sal=int(input("Enter amount to deposite "))
            print("Amount Deposite Succesfully ")
            salary=sal
        case 2:
            if salary==0:
                print("No balance avilable,Please first deposite ")
            else:
                amount=int(input("enter amount you want to withdrwal"))
                if amount<salary:
                    print("withdrwal succefully")
                    salary=salary-amount
                else:
                    print("insufficient balnce")
               
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