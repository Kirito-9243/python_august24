#Problem statement: Assume 1 and 2 are 1st 2 terms of the series and print the 1st N term of Fibo series (HemaChandra numbers)

fib_len = int(input("Enter the length if Fibo series:"))
first_term = 1
second_term = 2
print(first_term,second_term, end=" ")
for i in range(3,fib_len+1):
    current_term = first_term + second_term
    print(current_term, end=" ")
    first_term = second_term
    second_term = current_term

