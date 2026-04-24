class Parent():
    def __init__(self):
        print("Hello")

    def show(self):
        print("Parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Good Bye")

    def show(self):
        super().show()
        print("Child class")

obj=Child()
obj.show()
                             