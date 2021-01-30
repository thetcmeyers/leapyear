def leapYear(x):
    #if divisible by 4
    if x % 4 == 0:
        #if divisible by 100 anad not divisible by 400
        if x % 100 == 0 and x % 400 != 0:
            return False
        else:
            return True
    else:
            return False

go = True
while go:

    year = input("Enter the year:")

    try:
        val = int(year)
        if leapYear(val) == True:
            print("This is a leap year!")
            go = False
        else:
            print("This isn't a leap year :(")
            go = False
        
    except ValueError:
       print("Please enter an Integer")
    

