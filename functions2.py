import time

def func1():
    print("Hello world")
    time.sleep(2)
    print("The world is a beautiful place.")


def func2():
    print("Hello Universe")
    time.sleep(3)
    print("It is a pleasant day.")

def func3():
    print("Hello Cosmo")
    time.sleep(2)
    print("Trust the universe.")
    
t1=time.perf_counter()
func1()
func2()
func3()
t2=time.perf_counter()
print(t2-t1)