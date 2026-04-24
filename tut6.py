import time
name=input("Enter your name")
recenttime= time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
if(4<=hour<12):
    print('Good MOrning',"Sir",'its',recenttime)
elif(12<=hour<17):
    print('Good evening',"Sir",'its',recenttime)
else:
    print('Good night',"sir",'its',recenttime)

