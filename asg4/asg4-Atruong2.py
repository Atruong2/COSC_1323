# Assignment 4
# Atruong2
# 09/24/17

# This program asks the user to guess a number between 1 and 50 in as few attempts as possible. 
# The program also counts the number of user attempts to guess the number.
  
import random

def main():
    guessingGame()

def guessingGame():
        
        print("Welcome to the '\Guessing Game\'!")
        
        randomNumber = random.randint(1,50)
        guessesTaken = 0
        print('I am thinking of a number between 1 and 50.')

        while True:
            guessedNumber = input("Take a guess:")
            guessedNumber = int(guessedNumber)
            guessesTaken = guessesTaken + 1
        
            if guessedNumber == randomNumber:
                guessesTaken = str(guessesTaken)
                print('You got it in ' + guessesTaken + ' attempts!')
                break

            elif guessedNumber < randomNumber:
                print('Higher.')
    
            elif guessedNumber > randomNumber:
                print('Lower.')
                
main()