alpha={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"}
s=""
miss=""
while True:
    print("1 enter sentence ")
    print("2 display missing alphabet ")
    print("3 count missing alphabet")
    print("4 exit")
    choice=int(input('enter choice '))
    match choice:
        case 1:
            x = input("enter first string ")
            s=x
        case 2:
            
            for i in alpha:
                if i not in s:
                    miss+=i+" "
            print("missing alphabet is ",miss)    
        case 3:
            print("count of missing alphabet is ",len(miss))
        case 4:
            print("process exist5 ")
            break