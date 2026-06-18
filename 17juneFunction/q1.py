def registration(name,email,mobile,/):
    print("Name :",name)
    print("Email :",email)
    print("Mobile :",mobile)
    

def information(*,product,price,category):
    print("Product Name :",product)
    print("Price :",price)
    print("Category :",category)
    return

def default(product="laptop",price=55000):
    print("Product Name :",product)
    print("Price :",price)
    return 

def multiplevalue(*awrg):
    print("Total Bill Amount :",sum(awrg))

def detail(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    

def main():

    while True:
        print("===Mean===")
        print("1. Customer Registration ")
        print("2. Product Information")
        print("3. Generate Invoice")
        print("4. Add Multiple Products")
        print("5. Display Customer Profile")
        print("6. Exit")
       
        choice=int(input("Enter the Choice :"))

        match choice:
            case 1:
                print()
                name=input("Enter Name :")
                email=input("Enter Email :")
                mobile=input("Enter Mobile :")
                registration(name,email,mobile)
                print("Customer Registered Successfully")
            case 2:
                print()
                information(product="laptop",price=55000,category="Electronics")
                print("Product Detail Displayed Successfully")
            case 3:
                print()
                print(default())
                print("Invoice Generated Successfully")
            case 4:
                print()
                print(multiplevalue(100,200,300,400))
        
            case 5:
                print()
                print(detail(name="deepika",age=30,address="chennai"))

            case 6:
                print()
                print("Thank You . Program Terminated. ")
                break

            case _:
                print("Invalid choice")
main()

