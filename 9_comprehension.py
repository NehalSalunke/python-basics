### Comprehension

## 1. List comprehension
l1=[1,2,3,4,5]
print([x**2 for x in l1])
      #o/p - [1,4,9,16,25]
print([x**2 for x in range(1,31)])

print([chr(x) for x in range(65,90)])

# 1.1. comprehension with condition
print([x**2 for x in range(1,31) if x%2==0])
print([x**2 if x%2==0 else x**3 for x in range(1,31)])

# 1.2 convert integer list
l1=[1,2,3,4,5,6,7,8,9,10]
print(int(''.join([str(x) for x in l1])))
#print A-Z from list to joint string
print(''.join([chr(x) for x in range(65,91)]))
  

## 2. set comprehension
s1={1,2,3,4,5}
{x**2 for x in s1}
## 3. generator comprehension
(x**2 for x in l1)


## 4. dictionery comprehension
l2=[5,4,3,2,1]
print({x:x**2 for x in l2})
#using dictionery comprehension WAP to form dictionery like{1:'A',2:'B'....,26:'Z'}
print({x-64:chr(x) for x in range(65,91)})
#using dictionery coprehension WAP to inverse the dictionery
d1={1:2,3:4,5:6}
print({d1[x]:x for x in d1})

