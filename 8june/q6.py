s1=set()
s2=set()
while True:
    print("1 enter first string ")
    print("2 enter second string ")
    print("3 display common charter")
    print("4 count common char")
    print("5 exit")
    
    
    choice=int(input('enter choice '))
    
    match choice:
        case 1:
            x = input("enter first string ")
            for ch in x:
                if ch != " ":
                    s1.add(ch)

        case 2:
            t = input("enter second string ")
            for ch in t:
                if ch != " ":
                    s2.add(ch)
             
        case 3:
            print("the common charter are ",s1&s2)
            
        case 4:
            print("the count of commmon charter is ",len(s1&s2))
        
        case 5:
            print("process exist5 ")
            break