num = int(input("Enter a number:"))
rev=0
sum=0
while num>0:
    rem = num%10
    rev = (rev*10)+rem
    sum+=rem
    num=num//10
print("Sum is:",sum)
print("Reverse is:",rev)
