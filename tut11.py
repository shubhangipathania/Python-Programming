#functions in python
def calculategmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)

def greater(c,d):
    if(c>d):
        print("First no is greater than second.")
    elif(c==d):
        print("NUmber is equal.")
    else:
        print("First number is lesser than second.")


a=10
b=15
greater(a,b)
calculategmean(a,b)

g=34
j=89
greater(g,j)
calculategmean(g,j)

def greet(name):
    print("Good morning", name)

s= "Rohan"
greet(s)
