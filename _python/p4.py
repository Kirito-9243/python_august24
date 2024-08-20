#Problem statement:Program to Accept three distinct numbers and find the smallest among them

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))

#using builtin functions
print("Using builtin functions:")
print("The numbers are:",num1 ,num2 ,num3)
print("The smallest among them is",min(num1,num2,num3))

#using logic 
print("Using logic:")
if num1 < num2 and num1 < num3:
    print("The smallest among them is",num1)
elif num2 < num3:
    print("The smallest among them is",num2)
else:
    print("The smallest among them is",num3)
