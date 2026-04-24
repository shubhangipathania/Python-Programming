class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @staticmethod
    def greet():
        print("Good Morning")

    @classmethod
    def factory_method(cls,name,age):
        return cls(name,age)
    
    @classmethod
    def alterate_constructor(cls,string):
        name,age= string.split(",")
        return cls(name,int(age))
    

    
s1=Student("Shubhangi",20)
print(s1.name,s1.age)
Student.greet()

s2=Student.factory_method("Shreya",16)
print(s2.name,s2.age)
Student.greet()

string="Shivam, 20"
s3=Student.alterate_constructor(string)
print(s3.name,s3.age)
s3.greet()
