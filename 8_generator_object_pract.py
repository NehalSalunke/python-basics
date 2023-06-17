def sqlist(a):
    list=[]
    for each in a:
        list.append(a*2)
    return list
print(sqlist([1,2,3,4,5,6]))


def sqlist2(a):
    for each in a:
        yield each**2
result=sqlist2([1,2,3,4,5,6])
print(result)
print(next(result))
for each in result:
    print(each)

