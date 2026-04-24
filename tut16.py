#manipulation on tuples
tup1=(23,56,88,100,"Hello","Delhi",67,"Punjab","Dog","cat",55)
print(tup1)
lst=list(tup1)
print(lst)
lst.append("Spain")
lst.extend([3,6,7])
lst[6]=45
print(lst)
tup1=tuple(lst)
print(tup1)
print(tup1.count(56))
print(tup1.index("Delhi"))
print(tup1.index("Hello",2,6))