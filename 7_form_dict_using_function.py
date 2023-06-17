## write function to form dictionary from 2 list
## formdict ([1,2,3],[4,5,6])
##{1:4, 2:5, 3:6}
# if two list has different length return error
# if 1st list has duplicate value(which will be key of dictionary return error)


def formdict(a,b):
    if len(a)!=len(b):
        print("the two lists are not equal")
    elif len(a)!=len(set(a)):
        print("lists are not equal")
    else:
        result={}
        '''for k in a:
            for v in b:
                result[k]=v
        return result'''

        for each in range(len(a)):
            result[a[each]]=b[each]
        return result
            
            


print(formdict([1,2,3],[4,5,6]))
