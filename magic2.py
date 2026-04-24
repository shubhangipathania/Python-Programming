class Student:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def __repr__(self):
        return f"Student('{self.name}', {self.age})"
    
    def __len__(self):
        return len(self.name)
    
    def __call__(self):
        return f"This is the record of class Student."
    
    def __add__(self,other):
        return Student((self.name + other.name), (self.age + other.age))
    
s1=Student("Shivam",20)
print(s1)
print(repr(s1))
print(len(s1))
print(s1())
s2=Student("harry",27)
print((s1+s2).name, (s1+s2).age)