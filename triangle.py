a = int(input("Enter length of a:"))
b = int(input("Enter length of b:"))
c = int(input("Enter length of c:"))
if(a+b)>c and (a+c)>b and (b+c)>a:
    if a**2 + b**2 == c**2:
        print("It is a Right angled Triangle")
    else:
        print("It is not a Right angled Triangle")

else:
    print("given sides doesnot form a triangle")