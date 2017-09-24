import random
def main():
    
    counter = 1
    while( counter <= 5) :
        print("the value of counter is --> ", counter)
        print("\tI am in the while loop")
        counter = counter + 1
        number = random. randint(1,100) 
        print("The random number is   ", number)
        if( number % 7 == 0):
            print( number, "      is divisible by 7")
    


#print("I am just out of the while loop")
main()