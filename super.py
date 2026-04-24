class Teacher:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def showDetails(self):
        print(f"{self.name},{self.id},{self.salary}")

    def greet(self):
        print(f"Good Morning {self.name}")

class Student(Teacher):
    def __init__(self,name,id,salary,section):
        super().__init__(name,id,salary)
        self.section=section

    def show(self):
        super().showDetails()

    def greet(self):
        print("Good day!")
        super().greet()

    
t1=Teacher("Anuradha",2345,20000)
t1.showDetails()
t1.greet()

s1=Student("Shubhangi",278,30000,"A")
s1.show()
s1.greet()

