##Python Web Development Techdegree
##Project 1 - Number Guessing Game
##--------------------------------
import random
import time
import sys

HighScore = []

def start_game():
    TheNrToGuess = random.randint(1,10)
    UserInput = 0
    Guesses = 0

    if len(HighScore)>0:
        print("Highscore: ")
        listy = 1
        for score in HighScore:
            print(str(listy) + '. ' + str(score) + ' guesses')
            listy += 1
    
    while UserInput != TheNrToGuess:    
        UserInput = 0
        while UserInput == 0:
            try:
                UserInput = int(input("Guess a number between one and ten: "))
                if not 0 < UserInput < 11:
                    print("Only numbers ranging from 1 to 10 are allowed! Guess again.")
                    UserInput = 0
            except:
                print("Make sure to fill in a (whole) number please. Letters and other characters are not allowed")
        Guesses += 1
        if UserInput == TheNrToGuess:
            HighScore.append(Guesses)
            HighScore.sort()
            if Guesses == 1:
                print("Congratulations! The number was indeed {}. You guessed the number in {} guess!!!".format(TheNrToGuess, Guesses))
            else:
                print("Congratulations!  The number was indeed {}. You guessed the number in {} guesses.".format(TheNrToGuess,Guesses))
            if len(HighScore)>1 and Guesses < HighScore[1]:
                print("You just achieved the highest score since the game was started")
            break
        elif UserInput > TheNrToGuess:
            print("Sorry, that's not it. The number is lower than that.")
        else:
            print("Sorry, that's not it. The number is higher than that.")
        

print("Hi and welcome to Sebastiaan's number guessing game.")

start_game()

while input("Do you want to play again? (N/y)").lower() == 'y':
    print("Great choice! Here we go again :)")   
    start_game()

print("Thanks for playing Sebastiaan's guessing game. I hope you had fun :)")

sys.exit()
