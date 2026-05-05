num=input("enter a number ")
count=0
maxdiff=0
smooth=0
print("Differnece: ",end=" ")
for i in range(len(num)-1):
    digit1=int(num[i])
    digit2=int(num[i+1])

    diff=abs(digit1-digit2)
    print(diff,end=" ")

    if diff>2:
        count+=1
        smooth=1
    if diff>maxdiff:
        maxdiff=diff
print("\ncount >2 ",count)
print("max difference is ",maxdiff)
if smooth:
    print("irregular number ")
else:
    print("smooth number ")



        