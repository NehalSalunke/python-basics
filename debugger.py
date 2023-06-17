def add(a,b):
    mysum=a+b
    print(mysum)
    return mysum 

if __name__=='__main__':
    x=input("Enter first number")
    y=input("Enter second number")
    z=add(x,y)
    print("sum of x and y is ", z)
