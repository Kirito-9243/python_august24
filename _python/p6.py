# Program statement: Program to check if the Alphabet is uppercase

alpha = input("Enter any alphabet:")
if len(alpha) != 1:
    exit("Invalid input!!")
    
if alpha.isupper():
    print(alpha,"is an uppercase Alphabet")

