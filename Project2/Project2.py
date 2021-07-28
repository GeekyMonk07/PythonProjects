import random
randNumber = random.randint(1,100)
# print (randNumber)

guesses = 0
userGuess = None

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess : "))
    guesses += 1 
    if(userGuess == randNumber):
        print(f"Your Guess is Correct!")
    else:
        if(userGuess > randNumber):
            print("Wrong Guess! Enter a samller Number")
        else:
            print("Wrong Guess! Enter a larger Number")

print(f"Your score is {guesses} guesses!")

with open ("Project2/highscore.txt") as f:
    highscore = int(f.read())
if(guesses < highscore):
    print("You just broke the Highscore!!")
    with open ("Project2/highscore.txt",'w') as f:
        f.write(str(guesses))
