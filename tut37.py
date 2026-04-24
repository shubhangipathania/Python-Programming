#local and global variables
x=9  #global variable
y=5  #global variable
a=5  #global variable
print(a)
print(x)
print(y)




def hello():
    print("hello everybody")
    print("Good day everyone.")
    x=4
    print(x)
    print(y)
    global a
    a=1  #modify the value of global a  
    b=4  #local variable
    print(b)
    print(a)

    

hello()
print(a)