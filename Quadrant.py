x = int(input("Enter x :"))
y = int(input("Enter y :"))

if x>0 and y>0:
    print("First Quadrant")
elif x<0 and y>0:
    print("Second Quadrant")
elif x<0 and y<0:
    print("Third Quadrant")
elif x>0 and y<0:
    print("Fourth quadrant")
else:
    print("Point at orgin")
    