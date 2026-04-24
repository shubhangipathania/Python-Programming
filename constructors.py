class Students:
    def __init__(self, name, Id, Batch, Subject):
        self.name=name
        self.Id= Id
        self.Batch= Batch
        self.subject= Subject
        print("It is done!")
        print(f"{self.name},{self.Id},{self.Batch},{self.subject}")

    
    @staticmethod
    def greet():
        print("Hello Everyone!")

obj1=Students("Shreya", 345, 2027, "Humanities")
obj2=Students("Shivam", 677,2028, "Maths")
obj1.greet()
obj2.greet()
