### generator object
##old method
def sqlist(a):
    print("1st program")
    for each in a:
        return each**2
print(sqlist([11,22,33,44]))
    #o/p= 121
    

#modification 1:
def sqlist(a):
    empty=[]
    print("2nd program")
    for each in a:
        empty.append(a)
    return empty
print(sqlist([11,22,33,44]))


# effective method
def sqlist(a):
    print("3rd program")
    for each in a:
        yield each**2
result=sqlist([11,22,33,44])
print(result) 
for each in result:
    print(each)
list(result)

## generator object only executes one time

