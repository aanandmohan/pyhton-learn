data=input("enter data ")

print("alphabet" if ("a"<=data<="z" or "A"<=data<="Z") else"Number" if "0"<=data<="9" else"special chartecter")
# print("alphabet" if data in "abcdefghijklmnopqrstuvwxyz" else "Number " if data in"0123456789" else"Special Charcter ")