## write a program to reverse key and values from dictionery 
'''d1={1:2,3:4,5:6}
d2={}
for each in d1:
  d2[d1[each]]=each

print("d2 = ",d20) '''

######################################

## write a program to find max number from list using for loop

'''l1=[1,5,6,7,4,9,3]
max=l1[0]
for each in l1:
  
    if each> max:
        max=each
print(max)'''



######################################

## write a prgram to find out element given by the user in list or not using for loop

l1=[11,22,55,44,66,99]
element = int(input("enter any nymber : "))
count=0
for each in l1:
    count=count+1
    if each ==element:
        print("element",element,"is found at", count-1,"index")
        
        break
    
else:
    print("element not found")
