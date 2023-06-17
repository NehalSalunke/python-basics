
### wrong method
'''def sqlist(a):
    for each in a:
        return each**2'''


### correct method
def sqlist(a):
    res=[]
    for each in a:
        res.append(each**2)
    return res


limit=int(input("how many elements"))
res1=[]
for each in range(0,limit):
    ele=int(input("enter number:- "))
    res1.append(ele)
print(res1)
print(sqlist(res1))

