passs=input("enter password ")
count=0
special=False
if len(passs)>=8 or len(passs)<=15:
    if passs[0].isupper():
        for i in range(1,passs):
            ch=chr[i]
            if ch>='A' or ch<='Z':
                continue
            elif ch>='a' or ch<='z':
                continue
            elif ch>=0 or ch<=9:
                count+=1
            else:
                special=True
                
