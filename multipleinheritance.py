class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"The name of the employee is {self.name}")

class Developer:
    def __init__(self,language):
        self.language= language

    def show(self):
        print(f"The language used by the developer is {self.language}")

class Both(Employee,Developer):
    def __init__(self,name,language):
        self.name=name
        self.language= language

e1=Employee("Shubhangi")
e1.show()
d1=Developer("Python")
d1.show()
b1=Both("Shubhangi","Python")
print(b1.name, b1.language)
b1.show()
print(Both.mro())