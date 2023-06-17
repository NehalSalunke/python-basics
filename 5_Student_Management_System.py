# project 1 - student management system
# Question  - write a program of student management system which works on below fields
#             1. Add student
#             2. Remove Student
#             3. find student
#             4. Exit
#
# Answer    -
true=1
add={}
while true:
    print("1. Add student")
    print("2. Remove student")
    print("3. find student")
    print("4. show all")
    print("5. Exit")
    choice=int(input("enter choice: "))
    if choice==1:
        #stud{101:{'name':'nehal','age':23,'marks':{'M':99,'E':100}},102:{'name':'swara','age':23,'marks':{'M':79,'E':90}}}
        roll=int(input("enter roll number: "))
        add[roll]={}
        add[roll]['name']=input("enter name: ")
        add[roll_no]['age']
        add[roll]['marks']={}
        add[roll]['marks']['M']=int(input("enter maths score: "))
        add[roll]['marks']['E']=int(input("enter english score: "))
        
        print("student added succesfully!!!")
        
    elif choice==2:
        remove=int(input("enter the roll number of student to remove entry from database: "))
        for each in add:
            if remove==each:
                add[each]=0
                
        
    elif choice==3:
        find=int(input("find student by roll number:"))
        for each in add:
            if find==each:
                print(add[each])
    elif choice==4:
        print(add)
        
    elif choice==5:
        print("Thank You!!!")
        break
    else:
        print("please give appropriate choice")




