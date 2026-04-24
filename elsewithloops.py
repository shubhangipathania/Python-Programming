#We can use 'else' with for loop and while loop.
# The else part is executed when the loop is exhausted, but it is not executed when the loop is terminated by a break statement.

for i in range(10):
    print(i)

else:
    print("End of the loop")

i=0
while(i<10):
    print(i)
    i=i+1
else:
    print("End of the loop")