
age=[20,25,30,45,67,89,49,55,54,56,67,89,47,44,44,55,57,58,59,51,51,52,12,23,37,61,65,67,65,65,64]
k=set()
name=["ram","komal","vishnukant","sita"]

def removeduplicate(x):
    for i in x:
        k.add(i)
    return k

def secondhigh(t):
    b=t.sorted()
    n=len(b)
    return b[n-2]

def countsenior(x):
    count=0
    for i in x:
        if i>50:
            count+=1
    return count

def countNameStartWith(name):
    count=0
    for i in name:
        if i=="A" or i=="E" or i=="O" or i=="U" or i=="i":
            count+=1
    return count
def longestName(name):
    max=len(name[0])
    for i in name:
        if len(i)>max:
            max=len(i)
    return max


while True:
    print("1 second highset age ")
    print("2 count senior employy")
    print("e remove dulpicate age ")
    print("4 count name satrt with vowel ")
    print("5 longest name ")
    print("6 exit ")

    choice=int(input("enter choice "))
    match choice:
        case 1:
            t=secondhigh(k)
            print("the second highest age is ",t)
        case 2:
            n=[]
            n=filter(lambda a:a>50,age)
            print("number of employ whose age is >50 ",len(list(n)))

