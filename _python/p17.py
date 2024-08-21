#Program statement: Program to Find odd placed digits in a number

input_num = input("Enter the number to find odd place digits:")
odd_placed = []
for i in range(len(input_num)):
    if i%2 == 0:
        odd_placed.append(input_num[i])
print("The odd placed digits are:",odd_placed)