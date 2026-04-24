class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show(self):
        print(f"The details of the employee are: {self.name}, {self.id}.")
    

class Developer(Employee):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.language=language
        


    def show(self):
        super().show()
        return f"The language used by the developer is {self.language}"
        
    

e1=Employee("Shubhangi",12345)
print(e1.show())

d1=Developer("Shubhangi",12234,"Python")
print(d1.show())