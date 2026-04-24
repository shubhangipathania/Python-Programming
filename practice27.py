import random 

def game():
    print("we are starting the game")
    print("Your Score")
    score=random.randint(1,60)
    
    with open("hiscore.txt") as f:
        hiscore=(f.read())
        if(hiscore != ""):
            hiscore= int(hiscore)
        else:
            hiscore= 0

    print(f"Your score is: {score}")
    if((score) > (hiscore)):
        with open("hiscore.txt", 'w') as f:
            f.write(str(score))

    return score


game()