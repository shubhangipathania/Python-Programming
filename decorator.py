import random

def hello(func):
    def decorated(*args, **kwargs):
        num = random.randint(1,50)
        print(num)
        func(*args, **kwargs)
        num1= random.randint(51,70)
        print(num1)
    return decorated


@hello
def add(a,b):
    print(a+b)
    print("The function is calculated.")


add(5,10)

