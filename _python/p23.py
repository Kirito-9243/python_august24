#Program statement: Program to print X shape inside Hollow Square

num_lines = int(input("Enter the number of lines:"))
for i in range(1,num_lines+1):
    for j in range(1,num_lines+1):
        if j == 0 or j == num_lines - 1 or i == 0 or i == num_lines - 1:
            print("*",end=" ")
        elif j == i or j == num_lines - i - 1:
            print("*",end=" ")
        else:   
            print(" ",end=" ")
    print()
