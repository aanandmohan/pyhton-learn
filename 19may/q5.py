domain=input("enter domain ")
if domain.startswith('www') and domain.endswith('.com'):
    print("valid domain ")
else:
    print("not valid domain")