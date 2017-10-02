# inClass #1
# Atruong2

import random
def main():
    print("----------basicCounting-----------")
    basicCounting()
    print("----------advancedCounting--------")
    advancedCounting()
    print("-------------randomAdd------------")
    randomAdd()
 
def basicCounting():
    startNum = int(input("Enter a starting number: "))
    endNum = int(input("Enter an ending number: "))
    for nums in range(startNum,endNum):
        print(nums, end = " ")
        print()
                
def advancedCounting():
    startNum = int(input("Enter a starting number: "))
    endNum = int(input("Enter an ending number: "))
    userInput = input("Do you want to print only odd numbers or even numbers? Press 0 for odd or 1 for even.")
     
    if(userInput == "0"):
        for nums in range(startNum,endNum):
            if nums % 2 == 1:
                print(nums, end = " ")
            print()
          
    if(userInput == "1"):    
        for nums in range(startNum,endNum):
            if nums % 2 == 0:
                print(nums, end = " ")
            print()
   
def randomAdd():
    userInput = int(input("Enter a positive integer: "))
    randNum = random.randint(1,100)
    sum = (userInput + randNum)
    print("%d + %d = %d" %(userInput, randNum, sum))
    print()
        
main()


