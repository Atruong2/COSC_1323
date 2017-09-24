# Review: 

# The input() function:
# Print whatever string is in ()
# Wait for user input
# Return as a string

#Review Assignment 3:

def doTestTwo():
# True & False are boolean
# "true" & "false" are string
# True --> if value is nonzero, the statement will be true
# False --> if value is zero, the statement will be false
    hungry = True
    thirsty = False
    if (thirsty == True) and (hungry == True) :
        print("You are thirsty and hungry.")
        
    elif (thirsty == True) and (hungry == False) :
        print("You are thirsty but not hungry.")
    
    elif (thirsty == False) and (hungry == True) :
        print("You are not thirsty but you are hungry.")
        
    elif (thirsty == False) and (hungry == False) :
        print("You are not thirsty and not hungry.")
        
# Boolean Class Example:

def main(): 
    hungry = 10
    
    print("Data type of variable 'hungry' is --> ", type(hungry))

    if(hungry):
        print("I am hungry!!!")
    else: 
        print("I am NOT hungry!!!")
        
main()
    
    
def main(): 
    userInput = 0
    
    print("Data type of variable 'userInput' is --> ", type(userInput))

    if(userInput):
        print("Something is entered!!!")
    else: 
        print("Nothing is entered!!!")
        
main()

#
def addNum(firstNum, secondNum):
    result = firstNum + secondNum
    print("The result is --> ", result)
    
def subtractNum(firstNum, secondNum):
    result = firstNum - secondNum
    print("The result is --> ", result)   
    
def multiplyNum(firstNum, secondNum):
    result = firstNum * secondNum
    print("The result is --> ", result)
    
def divideNum(firstNum, secondNum):
    if(secondNum == 0):
    print("You cannot divide by zero.")
else:
    result = firstNum / secondNum
    print("The result is --> ", result)
    
# Print out a menu showing options to the user
# Get user input
# execute the relevant program from depending on the user input
#     if(userInput == 1):
#             addNum(    )

# The program goes into a while loop
# 1 --> Add
# 2 --> Subtract
# 3 --> Multiply
# 4 --> Divide
# 5 --> Exit   

# If the user inputs "5," then the program will exit the while loop

# Calculator Program

def main():
    
    
    option = 0
    while(option < 0):
        print("\n","$" *10, "First line in while loop", "$" * 10)
        option = myMenu()
        if(option == 0):
            continue
        if(option == $):
            break 
        
    firstNum = int(input())
    print("enter the second number.")
    secondNum = int(input())
    
    if(option == 1):
        myAdd
    
    
    
    
def myMenu():
    
    
    
    
    menuOption = int(input("Please enter a selection: "))
    if(menuOption == "")
        print("You just printed enter. Choices are 1-5.")
        menuOption = 0
        return menuOption
    else:
        menuOption = int(menuOption)
        
    if(menuOption < 1 or menuOption > 5):
        print("Sorry, invalid input - Choices are 1-5.")
        menuOption = 0
    
    return menuOption
    
    
    