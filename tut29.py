#custom errors in python
a=input("Enter the value of a btw 10-20:")
if(a!="quit"):
    raise ValueError("Invalid value")
else:
    print("It is valid.")


lst=[2,5,6,7,43,87]
print(lst)
if(len(lst)<7):
    raise IndexError("Invalid list")

name=input("Enter the value of name:")
if(name=="quit"):
    print("It is valid.")
else:
    raise NameError("It is not valid.")