'''
stud={}
stud[101]={}
stud[101]['name']='mayank'
stud[101]['marks']={}
stud[101]['marks']['M']=88
stud[101]['marks']['E']=99 '''

## take input from user and create dictionary of student management

#stud{101:{'name':'nehal','marks':{'M':99,'E':100}}

    stud={}
    num=input("enter the roll no:")
    stud[num]={}
    stud[num]['name']=input("enter name")
    stud[num]['marks']={}
    stud[num]['marks']['E']=int(input("enter marks for english"))
    stud[num]['marks']['M']= int(input("enter marks for maths"))

    print(stud)


