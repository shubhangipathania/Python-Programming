#Recursion in python
def factorial(num):
    if(num==0 or num==1):
        return 1 
    else:
        return num *factorial(num-1)
    
print(factorial(5))
print(factorial(23))
print(factorial(10))

def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
print(fibo(3))
print(fibo(7))