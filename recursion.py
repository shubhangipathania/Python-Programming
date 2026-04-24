#Program to get the sum of first n natural numbers using recursion.

def sum_of_natural_numbers(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return sum_of_natural_numbers(n-1)+n

num=int(input("Enter the number:"))
print(f"The sum of first {num} natural numbers is: {sum_of_natural_numbers(num)}")
