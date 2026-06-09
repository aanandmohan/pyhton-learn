'''5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.'''
book={1,2,3,4,5,6}
while True:
    print("1 add ibs number ")
    print("2 remove isbn")
    print("3 search isbn ")
    print("4 display isbn")
    print("5 count books")
    print("6 exist")
    
    choice=int(input('enter choice '))
    
    match choice:
        case 1:
            x=int(input('enter the ibsn number of book'))
            book.add(x)

            
        case 2:
            t=int(input("enter isbn number that you want to remove "))
            book.remove(t)
            print("remove isbn")
            
        case 4:
            for i in book:
                print(i)
            
        case 3:
            x=int(input("enter isbn "))
            if x in book:
                print("isbn found ")
            else:
                print("isbn not found")
        case 5:
            print("the count of book is ",len(book))
        case 6:
            print("process exist5 ")
            break

