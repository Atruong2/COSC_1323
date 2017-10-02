# Datatype: len()
# Sequence:
from unittest.test.testmock.testpatch import function
ListOfItems = len(1, 2, 10, 70, "dog", "cat")

for loop vs. while loop:

# Example 1
  
def main(): 
      
for x in listOfItems:
    len(1, 2, 10, 70, "dog", "cat")
    print(x,end = " --> ") # It will print the x and then whatever is in " " afterwards
    print(type(x))
    
    print("-" * 50)
    print("Type of listOfItems is ", type(listOfItems))
    print("The length of listOfItems is --> ", len(listOfItems)) # len(listOfItems) will print the total # of items in the sequence (in this case, it is 6)
    
main()
    
# For each iteration, x (or whatever variable name you have given) will be = to each item in the sequence
Ex) 
x = 1
x = 2
x = 10
etc. until goes through each item in the sequence

    while( )
# The while loop continuiously checks for the condition in ( ) until there is a break or if the condition becomes false

# str/string is a sequence of characters

# Example 2

def main(): 
    userInput = input("Please enter a word --> ") # Whatever is inside the ( ) is the argument 
    
for indChar in "help":
    print(indChar, end = "-->" )
    if indChar == "e":
        print("e is available in the given word")
    else:
        print("e is NOT available in the given word")
        
    print("-" * 50)
    
main()
# In Example 2, you cannot input an integer, only can input a sequence



# Functions:
input()
random.randint()
type()
print()
len()
float()
int()
range()



def main(): # main() is the calling function
    returnValue = functionOne(1,2,3)
    
def functionOne(1,2,3): # This is the called function that goes back through main() and returns the value
    
    return result



The range() function:
# Can take 1,2, or 3 elements and puts it in a sequence
# Only takes positive and negative integers, will not take float numbers

range(100) # --> will print sequence of 0 through 99

range(1,50) # --> will print sequence of 1 through 49

range(1,50,10) # --> 1,11,21,31,41
# 1 = beginning 
# 50 = end
# 10 = step

# Example 1

def main():
    
    for number in range(20,10,-1):
        print("number is -->", number)
    
main()


# Example 2

def main():
    
    num = 10/3
    print("the value of num is %7.2f" %num) # %7.2f --> will output: 3.33
     
    print("*" * 30)
    for number in range(1,5):
        print("number is -->", number)
    
main()


