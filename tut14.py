#List Methods
marks=[12,67,55,34,98,69,100]
print(marks)
marks.sort()
print(marks)
colors=['red','orange','green','blue']
colors.sort()
print(colors)
lst=[34,77,11,10,78,95]
lst.sort(reverse=True)
print(lst)
m=lst
m[0]=67
print(m)
print(lst)

animals=['tiger','lion','deer','cow','dog','cat']
animals.append('zebra')
print(animals)

animals.insert(4,'elephant')
print(animals)

animals.extend([35,78,22,67])
print(animals)
animals.reverse()
print(animals)
print(animals.index('dog'))
print(animals.count('cat'))
animals2=animals.copy()
print(animals2)
print(animals+animals2)