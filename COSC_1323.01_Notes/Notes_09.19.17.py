def main():
    
    var1 = 3
    while(var1 < 100):
        var1 = var1 + 5
        print("the sentry variable is --> ", var1)
        if(var1 > 30):
            print("$$$$$$ the sentry variable inside the if clause is --> ", var1)
            continue
        #if the condition is true, it skips anything below the continue operator (aka line 11)
#        and it goes back to the while loop and keeps executing to the first line because of the continue operator
#        If the condition is false, it will just end
#        If there is no continue operator, it will execute all lines of code
        print("the sentry variable is --> ", var1)


main()

