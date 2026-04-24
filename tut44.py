#Map function in python 
lst=[5,7,8,4,3,2,3,4,5,9]
tup=(4,6,3,2,3,4)
nlst=list(map(lambda x:x*x , lst))
print(nlst)
a= list(map(int, input().split()))
print(a)
#filter in python
f= list(filter(lambda x: x>=6,lst))
print(f)
#reduce in python
from functools import reduce
b=reduce(lambda x,y: x*y,tup)
print(b)

              