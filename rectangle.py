class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    @classmethod
    def create_default(cls):
        return cls(10,5)
    
    @classmethod
    def create_square(cls,side):
        return cls(side,side)
    
obj1=Rectangle(10,5)
print(obj1.width,obj1.height)

obj2=Rectangle.create_default()
print(obj2.width,obj2.height)

obj3=Rectangle.create_square(15)
print(obj3.width,obj3.height)