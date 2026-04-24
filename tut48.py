#constructors in python 
class Student:
     def __init__(self,name,occupation):
          print("Hello Everybody!")
          self.name=name
          self.occupation=occupation

     def study(self):
          print(f"{self.name} is a {self.occupation}")


s1=Student("HARRY","DEVELOPER")
s2=Student("SHUBHANGI","PYTHON DEVELOPER")
s1.study()
s2.study()


class Details:
    def __init__(self,animal,group):
        self.animal=animal
        self.group=group

obj1=Details("Crab","Crustaceans")
print(obj1.animal,"belongs to the group",obj1.group)




