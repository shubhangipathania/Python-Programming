a=True
print(a := False)
print(happy := 5)
numbers=[1,2,3,4,5]
while (n := len(numbers))>0:
    print(numbers.pop())

foods=[]
while (food := input("Enter your favorite food:")) != "quit":
    foods.append(food)

names=["Shubhangi","Shreya","Shivam","Aditya","Kritika"]
if(name := input("Enter your name:")) in names:
    print(f"Hello {name}")