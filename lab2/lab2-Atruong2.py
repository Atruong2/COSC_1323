#---------------------------------------------------------
# Lab #2 - Professor Sundara
# Introduces comments, printing, functions, and simple math operations.
#
# Instructions:
#
# 1) Start 'Eclipse' and create a new file 'File' -> 'New'
# 
# 2) Copy and paste the contents of this assignment into a new file created by Eclipse
# and save the file as 'lab2-yourSEUusername.py'
#
# 3) Each function below has a set of instructions in the comments. 
# Follow the instructions in the comments above each function and write the Python code 
# to complete the content of each function according to the instructions.
#
# 4) To minimize errors, it is suggested that you test your code after completing
# each function by choosing 'Run' -> 'Run'. Each function already
# has a print line telling you which function you are in, to help you track
# down errors. (This is not required for the program to work.)
#
# 5) Once all of the functions are working, submit your 'lab2-yourSEUusername.py'
# to Canvas and save a copy for your own records in Box.
#----------------------------------------------------------------


def main() :


 doMathOne()
 doMathTwo()
 doMathThree()
 doMathFour()


# ***********************************************************************
# doMathOne()
# Write a function that stores the value 5 in the variable 'num' and prints 
# the contents of 'num'
# then stores 7 in 'num' and prints the contents of 'num'.
#
# Hint: To print the contents of a variabe x: print(x)
# ***********************************************************************
def doMathOne() :
 print("Now in the doMathOne() function")
 num=5
 print(num)
 num=7
 print(num)

# ***********************************************************************
# doMathTwo()
# Write a function that adds 5 + 7 and stores the result in the variable 'mySum'
# then prints the contents of the variable 'mySum'
# ***********************************************************************
def doMathTwo() :
 print("Now in the doMathTwo() function")
 mySum=5+7
 print(mySum)


# ***********************************************************************
# doMathThree()
# Write a function that stores 5 in the variable 'num' and prints 'num'
# then stores num + 7 in the variable 'mySum' and prints the contents of 'mySum'
# 
# Hint: To add a number to what is already in variable a: a = a + (Number)
# ***********************************************************************
def doMathThree() :
 print("Now in the doMathThree() function")
 num=5
 print(num)
 mySum=num+7
 print(mySum)

# *********************************************************************** 
# doMathFour()
# Write a function that prints "13" + "16"
# and then prints 13 + 16 (without quotes)
# Now add 13 + 16 and store the result in a variable named "sum"
# The program should then print "13 + 16 = 29", in a way that uses
# the contents of sum.
#
# Hint: To print a string that includes double quotes, you can surround
# the string with single quotes.
# ***********************************************************************
def doMathFour() :
 print("Now in the doMathFour() function")
 print('\"13"  +  "16\"')
 print("13 + 16")
 sum=13+16
 print('"13 + 16 = ',sum,'"') 

main()