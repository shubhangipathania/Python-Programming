import random 
print("SNAKE-WATER-GUN")
print("Rules for the Game:")
print("1. 0--SNAKE ")
print("2. 1--WATER ")
print("3. 2--GUN ")
print("Let's get started...")
print("ROUND 1")
value=[0,1,2]
for i in value: 
 up=0
 cp=0
 user_input=int(input("The user input is:"))
 computer_input= random.choice(value)
 print("The computer input is:",computer_input)
 if(user_input and computer_input == 0):
  print("IT IS DRAW.")
 elif(user_input==0 and computer_input==1):
  up=up+1
  print("YOU WON")
  print(f"You won {up} points")
 else:
  print("ok")
  


