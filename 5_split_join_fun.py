##### Object functions ##########
##objects- list, tuple, dictionery, set, integer, float

##split and join the string

##method 1
'''name='python is very good language'
print(''.join(name.split()))

'''
##method 2
name="python is very good language"
name2=name.split()
print(name2)
#print(''.join(name2))

'''
name='nehal ashok salunke'
print('$'.join(name.split()))'''
#########################################


## write a program which will take filename from user and print its extension
'''
         #method 1
file_name=input("enter file name:")
l1=file_name.split('.')
print(l1[-1])
         #method 2
file_name=input("enter file name:")
print(file_name.split('.')[-1])     '''



###functions of tuple

'''t1=(22,55,88,44,11,22,66,55,22,22)
print(dir(t1))
print(help(t1.index))
print(t1.count(22))
print(t1.index(22))
print(t1.index(22,3))
print(len(t1))'''


#### apend()
'''l1=[55,66,77]
print(l1.append(99))
print(l1)
print(l1.append([88,99]))
print(l1)
print(l1.extend([88,66]))
print(l1)
print(l1.append('nehal'))
print(l1)
print(l1.extend('nehal'))
print(l1)


stud={101:{'name':'nehal','age':23,'marks':{'M':99,'E':100}},102:{'name':'swara','age':23,'marks':{'M':79,'E':90}}}

dir(stud)
'''
