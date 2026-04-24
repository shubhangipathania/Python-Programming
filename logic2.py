lst=[1,4,7,6,5,3,9,6,7]
for i in lst:
    if(i== max(lst)):
        lst.remove(i)
    
print(lst)
for i in lst:
    if(i== max(lst)):
        print(f"The second largest no of the list is {max(lst)}")    