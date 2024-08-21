#Program statement: Program to print X shape inside Hollow Square

num_lines = int(input("Enter the number of lines:"))
for i in range(1,num_lines+1):
    for j in range(1,num_lines+1):
        if j == 1 or j == num_lines or i == 1 or i ==num_lines:
            print("*",end=" ")
        elif j == i or j == num_lines+1:
            print("*",end=" ") 
        else:   
            print(" ",end=" ")
    
    print()
