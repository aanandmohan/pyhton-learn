'''1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.'''

coding=set()
rob=set()
while True:
    print("1 add member in coding club")
    print("2 add memebr in robitic club")
    print("3 dispaly student in a coding club")
    print("4 display student in robotic club")
    print("5 find student in both club")
    print("6 studeny in coding club")
    print("7 only in robitic club")
    print("8 diplay all uniqe member ")
    print("9 display total uniqe cmember ")
    print("10 exit ")
    choice=int(input('enter choice '))
    
    match choice:
        case 1:
            n=int(input("number of member "))
            for i in range(n):
                x=int(input("enter imember id "))
                coding.add(x)
        case 2:
            n=int(input("number of member "))
            for i in range(n):
                x=int(input("enter imember id "))
                rob.add(x)
        case 3:
            for i in coding:
                print(i)
        case 4:

            for i in rob:
                print(i)
        case 5:
            print(coding &rob)
        case 6:
            print(coding-rob)
        case 7:
            print(rob-coding)
        case 8:
            print( coding | rob)
        case 9:
            print(len(coding)+len(rob))
        case 10:
            print("process end")
            break
        