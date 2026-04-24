#Object oriented programming in Python
class Students:
    name="Rohan"
    Age=20
    dob=11105
    occupation="Student"
    def study(self):
        print("The Student Studies")
        print(f"{self.name} is a {self.occupation}")

s1=Students()
s2=Students()
s3=Students()
s1.name="Priya"
s1.age=19
s1.dob=555
s1.occupation="Teacher"
s1.study()
print(s1.name,s1.age,s1.dob,s1.occupation)
print(s2.name,s2.Age,s2.dob,s2.occupation)
s2.study()

