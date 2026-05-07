salary=0
hra1=0
da1=0
netsal=0
while True:
    print('Menu ')
    print('1Enter Basic Salary ')
    print("2calculate HRA (20%) and DA (10%)")
    print("3Calculate Net salray")
    print("4Tax calculation")
    print("5 display salry slip")
    print("6 exit")
    choice=int(input("enetr choice "))
   
    match choice:
        case 1:
            sal=int(input("enter Basic salary "))
            print("Basic Salary Enter succesfully")
            salary=sal
        case 2:
            if salary==0:
                print("Please enter Basic salry first")
            else:
                hra=(20/100)*salary
                da=(10/100)*salary
                hra1=hra
                da1=da
                print("HRA ",hra)
                print("DA ",da)
        case 3:
            if salary==0:
                print("plese enter basic salry first ")
            else:
                netsal1=hra1+da1+salary
                netsal=netsal1
                print("Net salary is ",netsal)
            
        case 4:
            if salary==0:
                print("please enter basic salry first")
            else:
                if netsal>50000:
                    tax=(10/100)*netsal
                    print("tax deduction is ",tax)
                else:
                    tax=(5/100)*netsal
                    print("tax deduction is ",tax)
            
        case 5:
            if salary==0:
                print("Enter basic salry first ")
            else:
                print("Basic salry is ",salary)
                print("HRA:",hra)
                print("DA:",da)
                print("NEt salary :",netsal)
                print("Tax:",tax)
                total=netsal-tax
                print("final salary is ",total)
        case 6:
            print("Exist program...Thankyou")
            break
        case _:
            print("Invalid choice Please try again")

            

