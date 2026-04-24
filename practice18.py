p1="Please Click on this"
p2="You won a lottery"
p3="Click this link"
p4="You are selected for a job"

message=input("Enter the message:")
if((p1 in message) or (p2 in message)or (p3 in message) or(p4 in message)):
    print("This is a spam message")

else:
    print("It is not a spam message.")