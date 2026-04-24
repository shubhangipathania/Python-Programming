class Employee:                            #parent class
    def __init__(self, name,id,campany):
        self.name=name
        self.id=id
        self.campany=campany

    def showDetails(self):
        print(f"{self.name}, {self.id},{self.campany}")

class Programmer(Employee):               #child class
    def showLanguage(self):
        print("The Language is Python. ")


obj1=Employee("Shubhangi", 12345, "Microsoft")
obj1.showDetails()
obj2=Programmer("Shreya",5666,"Google")
obj2.showDetails()
obj2.showLanguage()


