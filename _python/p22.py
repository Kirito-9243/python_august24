# Program statement: Program tp print X shape of N lines


num_lines = int(input("Enter the number of lines:"))
for i in range(num_lines):
    for j in range(num_lines):
        if j == i or j == num_lines-i-1:
            print("*",end=" ") 
        else:   
            print(" ",end=" ")
    
    print()

    
