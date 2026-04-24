a=17
print(type(str(17)))
print(type('17'))
name="Shubhangi"
print(len(name))
print(name.count('h'))
for i in name:
    print(i)
print(name.isprintable())
data='''THIS \
IS THE INFORMATION.'''
print(data.replace("THIS","HERE"))
print(data.capitalize())
print(data.find("IS"))
print(data.isalnum())
n=int(input("Enter any number:"))
match n:
     case 1:
          print("good work.")
     case 2:
          print("Excellent")
     case 3:
          print("Outstanding")
     case _:
          print("better")

def multi(x=34,y=45,*f):
     "It takes two inputs------------"
     product=x*y*f[0]*f[1]
     return product

a=multi(4,6,7,6,4)
print(a)
print(multi.__doc__)

lst=[2,6,5,4,"hii","good",True,0,(2,5,6),{6,9}]
print(lst[4][0])
lst.append("this")
print(lst)
lst2=lst.copy()

letter="Hello,my name is {} and I am a student of {}"
college="IPEC"
print(letter.format(name,college))

city1="Delhi"
city2="Himachal Pradesh"
info=f"I live in {city1} but i belong from {city2}"
print(info)
