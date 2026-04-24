class Person:
    def __init__(self,name,age,gender,career):
        self.name=name
        self.age=age
        self.gender=gender
        self.career=career

    def show_details(self):
        print(f"Name:{self.name},Age:{self.age},Gender:{self.gender},Career:{self.career}")

    def show_Person(self):
        print("It is the Class Person.")

class Employee(Person):
    def __init__(self,name,age,gender,career,campany):
        super().__init__(name,age,gender,career)
        self.campany=campany

    def show_details(self):
        super().show_details()
        print(f"Campany:{self.campany}")

    def show_Employee(self):
        print("It is class Employee.")

class Student(Person):
    def __init__(self,name,age,gender,career,hobbies):
        super().__init__(name,age,gender,career)
        self.hobbies=hobbies

    def show_details(self):
        super().show_details()
        print(f"Hobbies:{self.hobbies}")

    def show_Student(self):
        print("It is class Student.")

class Intern(Employee,Student):
    def __init__(self,name,age,gender,career,campany,hobbies,role):
        Person.__init__(self,name,age,gender,career)
        self.campany=campany
        self.hobbies=hobbies
        self.role=role

    def show_details(self):
        Person.show_details(self)
        print(f"Role:{self.role}")
        print(f"Campany:{self.campany}")
        print(f"Hobbies:{self.hobbies}")

    def show_Intern(self):
        print("It is the class Intern.")

p1=Person("Aditya",21,"Male","Business")
p1.show_details()

e1=Employee("Harsh",20,"Male","CA","Deloitte")
e1.show_details()
e1.show_Employee()
e1.show_Person()

s1=Student("Shubhangi",20,"Female","Corporate","Reading")
s1.show_details()
s1.show_Student()
s1.show_Person()

i1=Intern("Shubhangi",20,"Female","Corporate","Microsoft","Reading","Data Scientist")
i1.show_details()
i1.show_Employee()
i1.show_Intern()
i1.show_Person()
i1.show_Student()