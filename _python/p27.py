#Problem statement: Find the Nth Fibo term (assume 1 and 2 as 1st 2 terms)

input_num = int(input("Enter the number to find nth Fibo term:"))
first_term = 1
second_term = 2
fibo_count = 0
fibo_list = [1,2]
for i in range(3,input_num+1):
    current_term = first_term + second_term
    fibo_list.append(current_term)
    first_term = second_term
    second_term = current_term
print("The ",input_num,"th Fibo term is",fibo_list[-1])
