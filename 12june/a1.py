

"""
=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit
"""

p={101:{"name":"vishnu","age":19,"gender":"Male","disease":"Dibates","doctor":"Dr.sharma"},
   102:{"name":"vishnu","age":19,"gender":"Male","disease":"Dibates","doctor":"Dr.sharma"}
    
   }

while True:
    print("Add new patient")
    print("Search patient") 
    print("Update patient disease")
    print("Delete patient record")
    print("Display all patients")
    print("Count total patients")
    print("Display patients by disease")
    print("Display oldest patient")
    print("Display youngest patient")
    print("Exit")
    choice=int(input("Enter your choice: "))
    # give me in match case statement
    match choice:
        case 1: 
            id=int(input("Enter patient id: "))
            name=input("Enter patient name: ")
            age=int(input("Enter patient age: "))
            gender=input("Enter patient gender: ")
            disease=input("Enter patient disease: ")
            doctor=input("Enter patient doctor: ")
            # p[id]={"name":name,"age":age,"gender":gender,"disease":disease,"doctor":doctor}
            p[id]={"name":name,"age":age,"gender":gender,"disease":disease,"doctor":doctor}
            print("Patient added successfully")
        case 2:
            id=int(input("Enter patient id: "))
            if id in p:
                print("patinet name ",p[id]["name"])
                print("patitent age ",p[id]["age"])
                print("patient gender ",p[id]["gender"])
                print("patient disease ",p[id]["disease"])
                print("patient doctor ",p[id]["doctor"])
            else:
                print("patient not found")
        case 3:
            id=int(input("enter patient id "))
            if id in p:
                dis=input("enter new diseas ")
                p[id]["disease"]=dis
                print("disease update succesfully ")
            else:
                print("patinet not found ")
        case 4:
            id=int(input("enter patinet id "))
            if id in p:
                p.pop(id)
                print("patient  record delte successfully")
                
            else:
                print("patinet not found ")
        case 5:
            for k,v in p.items():
                print(k,":",v)
            
        case 6:
            print("the count of patient ",len(p))
        case 7:
            dis=input("enter diseases ")
            for k,v in p.items():
                if v["disease"]==dis:
                    print(k,":",v)
        case 8:
            old=0
            id=0
            for k,v in p.items():
                if v["age"]>old:

                    old=v["age"]
                    id=k
            print("the patinet name is ",p[id]["name"])
            print("the patinet age is ",p[id]["age"])
            print("the patient gender is ",p[id]["gender"])
            print("the patient disease is ",p[id]["disease"])
            print("the patient doctor is ",p[id]["doctor"])
        case 9:
            young=2000
            id=0
            for k,v in p.items():
                if v["age"]<young:
                    young=v["age"]
                    id=k
            print("the patinet name is ",p[id]["name"])
            print("the patinet age is ",p[id]["age"])
            print("the patient gender is ",p[id]["gender"])
            print("the patient disease is ",p[id]["disease"])
            print("the patient doctor is ",p[id]["doctor"])
        case 10:
            print("process end")
            break


                        


            

            





            

        


