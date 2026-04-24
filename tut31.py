choice=int(input("Enter what do you want to do: CODING(1) OR DECODING(2): "))
if(choice==1):
    message=input("Enter the message you want to code:")
    lst=list(message)
    if(len(lst)>=3):
       x=lst.pop(0)
       
       lst.append(x)
       r1=input("Enter 3 characters you want to add in the ending:")
       lst.extend(r1)
       r2=input("Enter the 3 characters you want to add at the start:")
       lst.insert(0,r2)
       message="".join(lst)
       print(message)

    else:
        print(message[::-1])

elif(choice==2):
    message2=input("Enter the coded message to decode:")
    #lst2=list(message2)
    if(len(message2)<3):
        print(message2[::-1])

    elif(len(message2)>=3):
        lst2=list(message2)
        lst2=lst2[3:]
        lst2.pop(-1)
        lst2.pop(-1)
        lst2.pop(-1)
        y=lst2.pop(-1)
        lst2.insert(0,y)
        message2="".join(lst2)
        print(message2)




       
       
       