class Student:
    def __init__(self,age,name):
        self.__age= age
        self.__name=name

    def __fulname(self):
        self.y=34
        return self.y

class Subject(Student):
    pass


obj=Student(20,"Apurva")
obj1=Subject(21,"Aman")
print(obj._Student__age)
print(obj._Student__name)
print(obj._Student__fulname())

# print(obj.__age)
# print(obj.__name)
# print(obj.__fulname())

# print(obj1.__age)
# print(obj1.__fulname())
