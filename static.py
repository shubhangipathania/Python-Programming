class Math:
    def __init__(self,num):
        self.num=num


    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def greet():
        return "Good morning"

    
    def addtonum(self,n):
        self.num=self.num + n


a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(3,5))
print(Math.add(3,4))
print(Math.greet())