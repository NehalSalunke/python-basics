### anagrams

a=input("insert 1st string ")
b=input("insert 2nd string ")

if sorted(a.lower())==sorted(b.lower()):
    print("the strings are anagrams")
else:
    print("the strings are not anagrams")
