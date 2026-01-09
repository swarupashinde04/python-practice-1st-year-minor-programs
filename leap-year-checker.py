y = int(input("enter the year : "))
if ( y % 400 == 0 ) or ( y % 4 == 0 and y % 100 != 0 ) :
    print(" it is a leap year")
else :
    print("it is not a leap year")
