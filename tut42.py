#Lambda function in python

def appl(fx,value1):
    return 6+ fx(value1)

print(appl(lambda x:x*x,2))


#lambda function to find value
value= lambda x: x*x
def value(x):
  return x*x
print(value(2))

print((lambda a,b,c: (a+b+c))(4,5,6))

