#Problem statement: Find the Nth Prime number

num_prime = int(input("Enter the number to Find the prime number that resides at that position:"))
prime_count = 0
if num_prime <= 0:
    exit("Invalid input!!")

first_prime = 2
while first_prime <= 100:
    prime = True
    for i in  range(2,int(first_prime*0.5)+1):
        if first_prime%i == 0:
            prime = False
            break
    
    if prime:
        prime_count += 1
        if prime_count == num_prime:
            print("The",num_prime,"th prime number is",first_prime)
            break
    first_prime += 1

