import random

comGuess=random.randint(0,100)

while True:
    userGuess=int(input("Guess a number between 0-100:"))
    if userGuess>100 or userGuess<0:
        print ("Chosse Between The range")
    elif userGuess>comGuess:
        print("Guess Lower")
    elif userGuess<comGuess:
        print("Guess higher")
    else:
        print("Congrats , You are correct")
        break

    
