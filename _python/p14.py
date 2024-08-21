#Problem statement: Program to find the second smallest digit in a number

input_num = input("Enter the number to Find the 2nd smallest digit:")
lists_digits = []
length = len(input_num)
for i in input_num:
    lists_digits.append(i)
smallest = min(lists_digits)

for i in range(1,length):
    smallest_2 = input_num[i-1]
    if  smallest > input_num[i]:
        smallest_2 = input_num[i]
        
print("The 2nd smallest digits in",input_num,"is",smallest_2)
#print(smallest)