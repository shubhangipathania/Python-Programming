#Program to find whether a given number is prime or not
n1=int(input("Enter any number:"))
for i in range(2,n1):
    if(n1%i==0):
        print("The number is not prime.")
        break
else:
    print("The number is prime.")

