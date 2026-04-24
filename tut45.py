#is vs == in python 
#integers are immutable
a=4
b=4
print(a==b)  #true because refering to the same memory locations
print(a is b )

c=5
d=8
print(c==d)
print(c is d )
#strings are immutable 
f="Shreya"
g="Shreya"
print(f is g) #true because refering to the same memory location
print(f ==g)
#list are mutable
v=[1,2,4,5]
j=[1,2,4,5]
print(v is j)  #false because refering to different locations
print(v==j)
#tuples are immutable
k=(3,5,6)
t=(3,5,6)
print(k is t) #true beacuse refering to the same memory locations
print(k==t)

l=(1,2,3,4,5,6,7,8,9)
p=(1,2,3,4,5,6,7,8,9)
print(l is p)
print(l==p)

a1=[56,78]
b1=a1
print(a1 is b1)
print(a1==b1)

r=None
s=None
print(r is s)
print(r is None)
print(r==s)