import random
def main():
    numOfTries = 1
    while(numOfTries <= 5):
        print("You are in Attempt # --> ", numOfTries)
        numOfTries = numOfTries + 1
        appInput = random.randint(1,6)
        userInput = int(input("Roll the dice and enter the number between 1 and 6."))
        if(userInput == appInput):
            print("You guessed right.")
        else:
            print("Your guess was wrong. The number generated was --> ", appInput)
    print("Thank you for playing with me!")

main()


def myMenu():
    myMenu()
    
def divideNum(firstNum, secondNum):
    result = firstNum / secondNum
    print()
    
    
    menuOption = int(input("Please enter a selection:   "))
    print(menuOption)