# Program statement: Program to print the Equi Lateral Triangle of N lines
"""
    *
   ***
  *****
 *******
*********
"""
num_lines = int(input("Enter number of lines:"))
for i in range(num_lines):
    for j in range(num_lines-i-1):
        print(" ",end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
        