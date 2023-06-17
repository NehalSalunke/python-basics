#### print sum of numbers from list



'''l1=[3,4,5,1,2,6]
i=0
sum = 0
while i<=len(l1):
    print(l1[i])
    sum=sum+l1[i]
    i=i+1
    
print(sum)'''



#######################################################

####write a program to find user given number is present in the list or not


l1=[1,3,5,7,9]
a=int(input("Enter any number: "))
i=0
while i<len(l1):
    if a==l1[i]:
        print("the number", a, "is fount in list at index",i+1)
        break
    i=i+1
else:
    print("number entered not found in list ")
 

