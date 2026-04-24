class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def show_details(self):
        print(f"The name of the animal is {self.name} and it's species is {self.species}")

class Mammals:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def show_details(self):
        print(f"The name of the mammal is {self.name} and it's species is {self.type}")

    def reproduction(self):
        print("They reproduce by themselves internally.")

class Dog(Animal,Mammals):
    def __init__(self,name,species,type,breed):
        Animal.__init__(self,name,species)
        Mammals.__init__(self,name,type)
        self.breed=breed
  
    def make_sound(self):
        print("Bark")

a1=Animal("Sheru","Tiger")
a1.show_details()
m1=Mammals("Meowbilli","Cat")
m1.show_details()
m1.reproduction()
d1=Dog("Alex","Dog","Dog","Golden Retriver")
d1.make_sound()
d1.show_details()
d1.reproduction()