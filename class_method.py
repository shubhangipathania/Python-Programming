class Employee:
    campany="Apple"   #class variable 
    def show(self):
        print(f"The name is {self.name} and the campany is {self.campany}")
    @classmethod
    def changeCampany(cls,newcampany):
        cls.campany= newcampany
    

    
e1=Employee()
e1.name="Harry"
e1.show()
e2=Employee()
e2.name="Shubhangi"
e2.show()
e2.changeCampany("Microsoft")
e2.show()
print(Employee.campany)