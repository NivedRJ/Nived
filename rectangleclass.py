class Rectangle:
    def __init__(self,height,width,corx,cory):
        self.height = height
        self.width =  width
        self.cory = cory
        self.corx = corx
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2*(self.height+self.width)
    def center(self):
        x = corx + self.width/2
        y = cory + self.height/2
        print("Center is at x =",x,"y =",y)
h = int(input())
w = int(input())
corx = int(input())
cory = int(input())
object1 = Rectangle(h,w,corx,cory)
area = object1.area()
perimeter = object1.perimeter()
object1.center()
print("area is:",area," ","perimeter is: ",perimeter)