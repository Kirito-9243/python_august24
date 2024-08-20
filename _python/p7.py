# Problem statement: Program to check if the number is Perfect square

import math as mt
pre_num = int(input("Enter any number:"))
pre_sq = mt.sqrt(pre_num)
if pre_num == (pre_sq)**2:
 print(pre_num,"is a Prefect square!!")

# Prefect number::
divisors = []
for i in range(1,pre_num):
    if pre_num % i == 0:
        divisors.append(i)
#print(divisors)
pre_sum = sum(divisors)
if pre_num == pre_sum:
    print(pre_num,"is a Prefect number!!")
