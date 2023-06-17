## square using while loop



#break statement
'''i=1
while i<=10:
    if i==7:
        break
    print("square of ", i, " is ", i**2)
    i=i+1
else:
    print("Success")'''



#############################################


#continue statement
i=1
while i<=10:
    if i==7:
        i=i+1
        continue
    print("square of ", i, " is ", i**2)
    i=i+1
else:
    print("Success")


##else is only executed for the while loop if and only if all the itirations of the wile loop are executed
