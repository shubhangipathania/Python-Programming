
#break and continue statements
for i in range(1,101,1):
    print(i)
    if(i==50):
        break
    else:
        print("okay")
print("Thankyou")

for i in [2,3,4,6,8,10]:
    if(i%2!=0):
        continue
    print(i)

#do-while loop through while,break and if statement
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break