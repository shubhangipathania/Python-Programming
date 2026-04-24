class Student:
    def __init__(self,name):
        self._name= name

    def _fulName(self):
        return "This is Done."
    

class Subject(Student):
    pass

obj=Student("Harry")
obj1=Subject("Apurva")
print(obj._name)
print(obj._fulName())
print(obj1._name)
print(obj1._fulName())