import pdb
pdb.set_trace()

def find_sum_of_digits(num):
    sum = 0
    while num != 0:
        remainder = num %10
        num = num //10
        sum +=remainder
    return sum

input_number = int(input("Enter anumber find sum of its digits:"))
sum_digits = find_sum_of_digits(input_number)
print(f"Sum of digits of {input_number} is {sum_digits}")

