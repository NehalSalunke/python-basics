### Factorial using function

## using for loop
def factnew(a):
    result =1
    for each in range(1,a+1):
        result = result*each
    return result
x=int(input("enter the number to find factorial : " ))
print(factnew(x))




## using while loop 
def fact(b):
    factorial=1
    i=1
    while i<=b:
        factorial=factorial*i
        i=i+1
    return factorial
print(fact(5))
