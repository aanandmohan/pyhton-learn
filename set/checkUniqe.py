s=input("enter string")
if len(s)==len(set(s)):
    print("all char are uniqe")
else:
    print("duplicate are present")