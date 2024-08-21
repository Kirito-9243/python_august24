# Problem statement: Program to find sum of digits os a number

sum_num = int(input("Enter number to find the sum of its digits:"))
sum_digits = 0
for i in range(1,sum_num +1):
    sum_digits += i
print("The sum of digits in the given number is",sum_digits)