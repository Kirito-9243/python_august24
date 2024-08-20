#Problem statement:Accept a number as input say 'x' and define a logic to get the output 'y'.
# The input can be only 0 or 1 and the output must be 1 if the input is 0 and viceversa 

x=int(input("Enter a number(Either 0 or 1):"))
y="Please enter a valid number"
if x==1:
    y=0
elif x==0:
    y=1
if y == 0 or y == 1:
    print("value of y =",y)
else:
    print(y)

