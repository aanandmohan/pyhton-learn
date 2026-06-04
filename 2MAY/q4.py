r=int(input("enter row "))
c=int(input("enter column "))
m=[]
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input("enter elemnt ")))
    m.append(row)

print(m)

while True:
    print("1 print main diagonal ")
    print("2 print secondary diagonal ")
    print("3 compare sum of diagonal ")
    print("4 exit ")
    choice=int(input("enter choice "))
    main=0
    sec=0
    match choice:
        case 1:
            dig=""
            for i in range(r):
                for j in range(c):
                    if i==j:
                        main+=m[i][j]
                        dig+=str(m[i][j])+" "
            print("the main diagonal is ")
            print(dig)
        case 2:
            diga=""
            for i in range(r):
                for j in range(c):
                    if i==c-j-1:
                        sec+=m[i][j]
                        diga+=str(m[i][j])+" "
            print("the secondary diagonal is ")
            print(diga)
        case 3:
            sum1=0
            sum2=0
            for i in range(r):
                for j in range(c):
                    if i==j:
                        sum1+=m[i][j]
                    if i==c-j-1:
                        sum2+=m[i][j]
            if sum1==sum2:
                print("both digonal are equal ")
            elif sum1>sum2:
                print("digonal of main is greater ")
            else:
                print("secondary digonal is greater ")




