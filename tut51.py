#Getters and Setters in Python
class Student:
    def __init__(self,name):
        self._name=name     #hidden data

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,newname):
        self._name=newname

obj1=Student("Rahul")
print(obj1.name)
obj1.name="Sneha"
print(obj1.name)
