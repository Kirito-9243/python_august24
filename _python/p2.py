#Problem statement: Read a number from the user and check if it is even number or not

#To read data from the the console,we can use input().however the input() always read only a string as usual with all other languages

my_number=int(input("Enter any number:"))

if my_number%2==0:
    print(my_number,"is an Even number!!!")
else:
    print(my_number,"is not an Even number!!!")
    