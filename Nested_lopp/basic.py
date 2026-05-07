'''s=1
while s<=3:
    print("student ",s)
    subject=1
    while subject<=5:
        print("subject ",subject,end=" ")
        print()
        chapter=1
        while chapter<=4:
            print("chapter ",chapter,end=" ")
            chapter+=1
        print()
        subject=subject+1
    s=s+1
    print()'''


# for s in range(1,4):
#     print("student ",s)
#     for sub in range(1,6):
#         print("subject ",sub,end=" ")
#         print()
#         for ch in range(1,5):
#             print("chapter ",ch,end="")
#         print()
#     print()

for i in range(1,4):
    print("student ",i)
    sub=1
    while sub<=4:
        print("subject ",sub)
        sub+=1
    print()
        