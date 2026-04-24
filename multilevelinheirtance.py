class Human:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def show_details(self):
        print(f"Name:{self.name}, Gender:{self.gender}, Age:{self.age}")

    def eat(self):
        print(f"The human eats well.")

    def workout(self):
        print(f"The human workout really well.")

class Employee(Human):
    def __init__(self,name,gender,age,campany):
        super().__init__(name,gender,age)
        self.campany=campany

    def show_details(self):
        super().show_details()
        print(f"Campany: {self.campany}")

    def work(self):
        print("The employee works well.")

    def salary(self):
        print("The employee has a good amount of salary also.")

class Programmer(Employee):
    def __init__(self,name,gender,age,campany,language):
        super().__init__(name,gender,age,campany)
        self.language=language

    def show_details(self):
        super().show_details()
        print(f"Language: {self.language}")

    def coding(self):
        print("The programmer codes clean and well.")

    def play(self):
        print("The programmer plays really well.")

h1=Human("Shubhangi","Female",20)
h1.show_details()
h1.eat()
h1.workout()

e1=Employee("Shreya","Female",16,"Google")
e1.show_details()
e1.work()
e1.salary()
e1.eat()
e1.workout()

p1=Programmer("Shubhangi","Female",20,"Microsoft","Python")
p1.show_details()
p1.coding()
p1.play()
p1.eat()
p1.salary()
p1.workout()