def rem(l, word ):
    n=[]
    for items in l:
        if not(items == word):
            n.append(items.strip(word))
    return n

l=["Riya","Soham","Smriti","Apurva","Shubhangi","am"]
print(f"The new list is: {rem(l, "am")}")
