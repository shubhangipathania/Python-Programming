#Exception handling in python
a=input("Enter the number:")
print(f"Multiplication of {a} is:")

try:
   for i in range(1,11):
     print(f"{int(a)}x{i} = {int(a)*i}")
except ValueError:
   print("Invalid Syntax")
except NameError:
   print("Wrong Name")
except IndexError:
   print("invalid index")
    
print("The program terminates here")
print("thankyou")
#finally block
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")

