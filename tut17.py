print("KAUN BANEGA CROREPATI")
print("Lets play this!")
questions=["What is the chemical fomula of water?","Who is the developer of Python?","What is the capital of India?","WHat is the area of rectangle?"]
answers=["H2O","GUIDO VAN ROSSUM","DELHI","lENGTH*BREADTH"]

print(questions[0])
a=input("ENTER YOUR ANSWER:")
if (a=="H2O"):
    print("YOU WON 5000 RUPEES")
else:
    print("YOU LOSE")


    
print(questions[1]) 
b=input("ENTER YOUR ANSWER:")
if b in answers:
    print("YOU WON 7000 RUPEES")
else:
    print("YOU ARE TAKING 5000 RUPEES TO YOUR HOME.")
    
print(questions[2])
c=input("ENTER YOUR ANSWER:")
if c in answers:
    print("YOU WON 10,000 RUPEES")
else:
    print("YOU ARE TAKING 7000 TO YOUR HOME")

print(questions[3])
d=input("ENTER YOUR ANSWER:")
if d in answers:
    print("YOU WON 5 LAKHS.")
    print("CONGRATULATIONS")
