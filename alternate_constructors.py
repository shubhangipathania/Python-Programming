class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def from_str(cls,data):
        return cls(data.split("-")[0],int(data.split("-")[1]))

e1=Employee("Harry",10000)
print(e1.name,e1.salary)

data= "Shubhangi-15000"
e2=Employee.from_str(data)
print(e2.name, e2.salary)

data1="Shreya-15000"
e3=Employee.from_str(data1)
print(e3.name, e3.salary)
