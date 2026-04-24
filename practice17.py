#Greatest number from 4 numbers
a1=int(input("Enter the first number:"))
a2=int(input("Enter the second number:"))
a3=int(input("Enter the third number:"))    
a4=int(input("Enter the fourth number:"))
if(a1>a2):
    if(a1>a3):
        if(a1>a4):
            print("The greatest number is:",a1)
        else:
            print("The greatest number is:",a4)
    elif(a1<a3):
        if(a3>a4):
            print("The greatest number is:",a3)
elif(a1<a2):
    if(a2>a3):
        if(a2>a4):
            print("The greatest number is:",a2)     
        elif(a2<a4):
            print("The greatest number is:",a4)
    elif(a2<a3):
        if(a3>a4):
            print("The greatest number is:",a3)
        elif(a3<a4):
            print("The greatest number is:",a4)