#enumerate function in python
lst=[34,67,89,"Riya","Shruti","True"]
index=0
for i in lst:
    print(i)
    print(index)
    index=index+1

lst2=[34,66,23,76,"harsh","Abhishek","False"]
for index,i in enumerate(lst2,start=1):
    print(index,i)    

String="Hello my beautiful people"
for index,word in enumerate(String):
    print(f"The {word} is present at {index} index")