#Program statement: Program to find odd place even digits

input_num = input("Enter the number to find odd place even digits:")
odd_placed = []
for i in range(len(input_num)):
    if i%2 == 0:
        if int(input_num[i])%2 == 0:
            odd_placed.append(input_num[i])
print("The odd placed even digits are:",odd_placed)