class Rectangle:
    def __init__(self,width,height):
        self.width= width
        self.height=height

    @classmethod
    def default(cls):
        return cls(10,5)
    
r1=Rectangle.default()
print(r1.width,r1.height)