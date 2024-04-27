str1 = input("enter string:")
cons = 0
vow = 0
list1 = ['a','e','i','o','u']
for i in str1:
    if i in list1:
        vow+=1
    else:
        cons+=1
print("Vowels is :",vow)
print("Consonats is :",cons)

