class Records:
    def __init__(self,name,rollno,marks):
        self._name=name
        self._rollno=rollno
        self._marks=marks

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,newname):
        self._name=newname

    @property
    def rollno(self):
        return self._rollno
    
    @rollno.setter
    def rollno(self,newrollno):
        self._rollno=newrollno

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self,newmarks):
        self._marks=newmarks

obj1=Records("Sahil",7,89)
obj2=Records("Neha",3,99)
obj1.name="ajay"
obj2.rollno=8
obj1.marks=77
print(obj1.name,obj1.rollno,obj1.marks)
print(obj2.name,obj2.rollno,obj2.marks)
