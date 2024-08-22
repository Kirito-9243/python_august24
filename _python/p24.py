#Problem statement: Check if a number is Prime

num_prime = int(input("Enter a number to check if it is Prime:"))
if num_prime in [2,3,5]:
    print(num_prime,"is a Prime Number!!!")
elif num_prime%2 != 0 and num_prime%3 != 0 and num_prime%5 != 0:
    print(num_prime,"is a Prime Number!!!")