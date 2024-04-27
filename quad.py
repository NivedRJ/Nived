import math
a = int(input("Enter coeff of a :"))
b = int(input("Enter coeff of b :"))
c = int(input("Enter coeff of c :"))

d = b**2-4*a*c

if(d>=0):
    root1 = (-b + math.sqrt(d)/(2*a))
    root2 = (-b - math.sqrt(d)/(2*a))
    print("Root1 is :",root1)
    print("Root2 is :",root2)
else:
    print("roots are imaginery")