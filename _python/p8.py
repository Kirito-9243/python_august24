# Problem statement: Program to check the User given year is a leap year 

year = int(input("Enter any year:"))
if year % 4 == 0 or year % 400 == 0:
    print(year,"is a leap year!!")
