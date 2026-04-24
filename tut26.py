#Python else in loop
for i in range(6):
    print(i)
else:
    print("Invalid")

y=0
while(y<5):
    print(y)
    y=y+1
    if(y==3):
        break
else:
    print("Successful")

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")