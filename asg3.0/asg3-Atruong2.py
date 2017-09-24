# Assignment 3 
# Atruong2

def main(): 
    doTestOne()
    doTestTwo()
    doTestThree()

# The doTestOne() function prompts the user for a number.
# The input() function retrieves the number entered and stores it in a variable called "userInput."
# The number is converted from text to an integer through the int() operator.
# The modulo operator evaluates to True when the remainder of x divided by 2 is 0.
# The modulo operator evaluates to False when the remainder of x divided by 2 is greater than 0.
# If the number is even, the program will print "Number entered is even." If the number is odd, the program will print "Number entered is odd."

def doTestOne():
    userInput = input("Please enter an integer.")
    userInput = int(userInput)
    if(userInput % 2 == 0):
        print("Number entered is even.")
    else:
        print("Number entered is odd.")

# The doTestTwo() function tests the variables, 'hungry' and 'thirsty' for all possible 'True' and 'False' combinations.
# 'hungry' is set to True.
# 'thirsty' is set to False. 
# The 'if' and 'elif' statements set up the conditions that will print whether the user is hungry and/or thirsty.
# If 'thirsty' is true and 'hungry' are both true, the program will print "You are thirsty and hungry."
# If 'thirsty' is true and 'hungry' is false, the program will print "You are thirsty but not hungry."
# If 'thirsty' is false and 'hungry' is true, the program will print "You are not thirsty but you are hungry."
# If 'thirsty' and 'hungry' are both false, the program will print "You are not thirsty and not hungry."

def doTestTwo():
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
 
# The doTestOne() function prompts the user for a number.
# The input() function retrieves the number entered and stores it in a variable called "userInput."
# The number is converted from text to an integer through the int() operator.
# The 'if' and 'elif' statements determine if the number entered is divisible by 2 and/or 3. 
# If the number has no remainder when divided by 2 and 3, the program will print "The number is divisible by 2 and 3." 
# If the number has no remainder when divided by 2 but a remainder when divided by 3, the program will print "The number is divisible by 2 and not 3."
# If the number has no remainder when divided by 3 but a remainder when divided by 2, the program will print "The number is divisible by 3 and not 2."

def doTestThree():
    userInput = input("Please enter an integer.")
    userInput = int(userInput)
    if(userInput % 2 == 0) and (userInput % 3 == 0):
        print("The number is divisible by 2 and 3.")
    if(userInput % 2 == 0) and (userInput % 3 > 0):
        print("The number is divisible by 2 and not 3.")
    if(userInput % 3 == 0) and (userInput % 2 > 0):
        print("The number is divisible by 3 and not 2.")

main()