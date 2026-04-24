# Remove duplicates from a list without using set.
lst=[1,2,34,44,50,28,50,7,2,34]
print("The original list was:",lst)
for i in lst:
    if(lst.count(i)>1):
        lst.remove(i)
    else:
        ""
print(f"The new list is {lst}")    