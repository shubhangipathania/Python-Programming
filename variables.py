class Student:
    College="Inderprastha Engineering College"
    Course="BTech"
    noofstu=0
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
        Student.noofstu+=1

    def showdetails(self):
        print(f"The name of the student is {self.name}, the branch of the student is {self.branch}.")
        print(f"They belong to {self.Course} from {self.College}.")
        print(f"The total no of student are {self.noofstu}")

Student.Course="B.Tech"
stu1=Student("Shubhangi","AIML")
stu1.College="Indraprastha Engineering College"
stu1.showdetails()
stu2=Student("Apurva","AIML")
stu2.showdetails()
