class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return (self.x * self.y)
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14 * super().area()
    


c1=Circle(5)
print(c1.area())
    
s1=Shape(23,7)
print(s1.area())