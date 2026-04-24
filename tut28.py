#finally block in error handling
def func1():
 try:
    l=[1,2,3,4,5]
    i=int(input("Enter the index:"))
    print(l[i])
    return 1 
 except:
    print("Invalid Syntax")
    return 0
 finally:
    print("This is an important message.")

x=func1()
print(x)