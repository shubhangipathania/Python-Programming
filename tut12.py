#default arguments
def name(fname="ravi",mname="kumar",lname="Sharma"):
    print("Hello", fname,mname,lname)

name("abhishek","singh","Rajput")

def add(a=12,b=45):
    result=a+b
    print(result)


add(23)
#KEyword arguments
def name(fname,mname,lname):
    print("HEllo",fname,mname,lname)

name(mname="Peter", lname="wilison", fname="John")

def add(a,b):
    result=a+b
    print(result)

add(b=23,a=77)
#required arguments
def name(fname,mname,lname):
    print("Hello", fname, mname,lname)

name("Peter","jack","john")
#variable length arguments
def name(*name):
    print("Hello",name[0],name[1],name[2],name[3])

name("ria","pia","jia","isha")


def add(a,b,*c):
    result=a+b+c[0]+c[1]+c[2]
    print(result)

add(2,3,4,5,6)


def name(**name):
    print("Hello", name["fname"], name["mname"],name["lname"])

name(mname="Singh", lname="Pathania", fname="Rudra")


def add(a,b):
    result=a+b
    return result

c= add(14,56)
print(c)

