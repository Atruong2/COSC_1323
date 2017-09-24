def main():
    reco = tempConversion( 100, "dry")
    print(reco)
    reco = tempConversion2
    if reco > 2:
        print 
#Pass the value of C
#Convert into F
#Return this value
       
def tempConversion( celsius, atmosphere ):
    farenheit = (1.8 * celsius) + 32
    if (atmosphere == "dry") and (farenheit > 90):
        return "it is hot and dry! You need air conditioning"
    elif (atmosphere == "dry") and (farenheit > 50):
        return "it is cold and you need a sweater"
    elif (atmosphere == "humid") and (farenheit > 90):
        return "it is miserable. maybe you need to go for a swim"
    else:
        return ""

main()        