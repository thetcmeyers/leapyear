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

year = int(input("Enter the year:"))

if leapYear(year) == True:
    print("This is a leap year!")
else:
    print("This isn't a leap year :(")
