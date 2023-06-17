### ZIP
'''
l1=[1,2]
l2=[3,4,5,6]
print(list(zip(l1,l2)))
print(dict(zip(l1,l2)))
print(tuple(zip(l1,l2)))
print(set(zip(l1,l2)))
'''

### MAP
'''
def sqlist(num):
    return num**2
print(list(map(sqlist,[1,2,3,4,5])))
print(list(map(sqlist,range(1,50))))

stmt="python is very easy language"
stmt.split()
print(list(map(len,stmt.split()))
print(list(sum(map(len,stmt.split()))))'''

# use map function to create or print A-Z list 
#print(list(map(chr,range(65,91))))


### lambda function
#print(list(map(lambda a:a**2, range(1,50))))

'''l1=[1,2,3]
l2=[4,5,6]
print(list(map(lambda a,b:a+b,l1,l2)))



from functools import reduce
l1=[1,2,3,4,5]
print(reduce(lambda a,b:a+b,l1))
# factorial program using reduce
num=5
print(reduce(lambda a,b:a*b, range(1,num+1)))
'''

### FILTER
#print the numbers devisible by 7 from 1-200
print(list(filter(lambda a:a%7==0,range(1,200))))








