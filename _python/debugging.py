
import pdb

pdb.set_trace()

def find_factorial_iteratively(num):
    fact = 1
    if num == 0 or num == 1:
        return fact 
    else:
        for i in range(2,num+1):
            fact *= i
        return fact

def find_factorial_recursively(num):
    fact = 0
    if num == 0 or num == 1:
        return 1
    else:
        return num *find_factorial_recursively(num-1)


input_num = int(input("Enter a number to find its factorial:"))
choice = int(input("1.iterative\n2.recursive\nEnter your choice:"))
fact = 0
if choice == 1:
    fact = find_factorial_iteratively(input_num)
    print(f"The factorial of {input_num} iteratively is {fact}")
elif choice == 2:
    fact = find_factorial_recursively(input_num)
    print(f"The factorial of {input_num} recursively is {fact}")
else:
    print("Invalid choice")

