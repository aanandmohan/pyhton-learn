type=input("enter user type ")
amount=int(input("enter total amount "))

print("20% dicount" if type=="premium" and amount>5000 else"10% dicount" if type=="regular" and amount>3000 else"5% discount" )