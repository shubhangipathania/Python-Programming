names= ["Harsh", "Priya", "Isha","Shreya","Shubhi","Shivam"]
print(names)
names[4]="Aditya"
print(names)

#assessing the list items using index
print(names[0])
print(names[5])
print(names[-3])



#to check if an element is present in the list
if "Shivam" in names:
    print("Shivam is present.")

else:
    print("Shivam is absent.")

if "riya" in names:
    print("Riya is present.")
else:
    print("Riya is absent.")

lst1=['Good', 78, "JIYA", 123, "monkey","mango", 55, 'bye']
print(len(lst1))
print(lst1[1:6])
print(lst1[0:9])
print(lst1[4:8])
print(lst1[:])
print(lst1[:6])
print(lst1[3:])
print(lst1[-6:-3])
print(lst1[-8:-5])
print(lst1[-1:])
print(lst1[1:7:2])
print(lst1[4:7:3])
print(lst1[-4:-2:2])

#list comprehension
marks=[56,78,33,98,22,45,77,45,72,34,44,90,66,11,55]
marks1=[mark for mark in marks if mark>30]
print(marks)
print(marks1)


str=["Riya","GOAt", "Cap","world","dog","what","animal"]
str1=[item for item in str if 'a' in item]
print(str)
print(str1)


