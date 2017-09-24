# Lab #3
# Atruong2

def main():
#Displaying Welcome Message
    print("This Tipper program can be used to help split a restaurant bill between friends, and also suggests the percentage tip.")
    
#Taking user inputs for all variables
    finalBillAmount = float(input("Enter the final bill amount."))
    numberOfPeople = int(input("Enter the number of people splitting the bill."))  
    
#Taking internal calculations and displaying final values on screen   
    print("Final Bill Amount = $", finalBillAmount)
    smallTip = (finalBillAmount * 0.15) + (finalBillAmount) 
    print("Final Bill Amount + 15% tip = $", finalBillAmount)
    largeTip = (finalBillAmount * 0.20) + (finalBillAmount)
    print("Final Bill Amount + 20% tip = $", finalBillAmount)
    print("Number of people splitting the bill =", numberOfPeople)
    print("Each person's share of the actual final bill without including the tip = $", float(finalBillAmount / numberOfPeople))
    print("Each person's share with 15% tip included = $", smallTip / numberOfPeople)
    print("Each person's share with 20% tip included = $", largeTip / numberOfPeople)

main()