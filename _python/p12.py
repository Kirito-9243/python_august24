# Problem statement: Program to Find count of digits of a number

input_num = input("Enter the number to Find digits of it:")
#frequency = []
for i in input_num:
    count_digits = input_num.count(i)
    #frequency.append(count_digits)
    print("The digit",i,"is repeated",count_digits,"times!")
    count_digits = 0
#print(set(frequency))
    