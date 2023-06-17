### parametorised functions

def calculator(a,b,c):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="*":
        return a*b
    elif c=="/":
        return a/b

d=int(input("enter 1st value"))
e=int(input("enter 2nd value"))
print(calculator(d,e,"*"))
