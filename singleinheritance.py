class Animal:
    def __init__(self,name,species):
        self.name= name
        self.species= species

    def make_sound(self):
        print(f"Sound made by the animal {self.name}.")

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed= breed

    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)

    def make_sound(self):
        print(f"Meow by {self.name} {self.species}")


a1=Animal("Joy","Dog")
a1.make_sound()
d1= Dog("Alex", "Dog", "Golden Retriever")
d1.make_sound()
c1=Cat("Judo","Persian")
c1.make_sound()