#Problem statement: Program to print right angled triangle
"""
#
##
###
####
#####
.........
"""
length = int(input("Enter the length of the triagnle:"))
for i in range(length+1):
    print("#"*i,"\n",end=" ")
