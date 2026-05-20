passs=input("enter username ")
digit=0
space=0
under=0
if len(passs)>=5 or len(passs)<=15:
    if passs[0]>='a' and passs[0]<='z':
        for i in range(1,len(passs)):
            if passs[i]>='0' and passs[i]<='9':
                digit=1
            elif passs[i]==' ':
                space=1
                
                break
            elif passs[i]=="_":
                under=1
        if digit==1 and under==1 and space==0:
            print("valid username")
        else:
            print("not valid user name ")
    else:
        print("not valid user name ")
else:
    print("not sufficent length")

    
        