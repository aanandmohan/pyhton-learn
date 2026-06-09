'''4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed'''
sub=frozenset(["python","java","mySql","react","springboot"])
while True:
    print("1 display subject")
    print("2 searxh subject")
    print("3 count subject")
    print("4 attempt to add subject")
    print("5 exit")
    
    choice=int(input('enter choice '))
    
    match choice:
        case 1:
            for i in sub:
                print(i)
        case 2:
            s=input("enter subject you want to search")
            if s in sub:
                print("course present")
            else:
                print("course not present")
        case 4:
            print("adding subject is not possible ")
        case 3:
            print("th ecount of subjec is ",len(sub))
        case 5:
            print("process exit ")
            break

