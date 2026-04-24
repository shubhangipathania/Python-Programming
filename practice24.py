#Program to find the temp in celcius 

def temp_in_celcius(temp):
      c=(5*(f-32)/9)
      return c

f=int(input("Enter the temperature in F:"))
print(f"The temperature in celcius is: {temp_in_celcius(f)} ")
