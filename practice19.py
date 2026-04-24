username=input("Enter the username:")
if(len(username)<10):
    print("Username has less than 10 characters.")
elif(len(username)==10):
    print("Username has exactly 10 characters.")
else:
    print("Username has more than 10 characters.")