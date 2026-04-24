class Employee:
    def __init__(self,name,eid,campany):
        self.name=name
        self.eid=eid
        self.campany=campany

    def __str__(self):
        return f"The details of the employee are {self.name},{self.eid},{self.campany}"
    
    def __repr__(self):
        return f"Employee('{self.name}',{self.eid},'{self.campany}')"
  
    def __len__(self):
        return len(self.name)
    
    def __call__(self):
        return "This is the information of an employee."
    
e1=Employee("Ranjit",2567,"ATOZ")
print(e1)
print(repr(e1))
print(len(e1))
print(e1())