#loops in python
#for loop
name= "Shubhangi"
for letter in name:
    print(letter)

name2= "Shreya"
for i in name2:
    print(i)
    if(i=='y'):
        print("it is y")
    elif(i=='e'):
        print("it is e")

lst=['mango', 'apple', 'grapes', 'banana', 'pineapple']
for fruit in lst:
    print(fruit)
    for i in fruit:
        print(i)

for num in range(1,20):
    print(num)

for k in range(10,30,2):
    print(k)