#Program statement:Find sum of series n + n(2) +n(3) + ...... m terms

print("Find sum of series n + n(2) +n(3) + ...... m terms")
multiple = int(input("Enter the multiple:"))
num_terms = int(input("Enter the number of terms:"))
sum_series = 0 
for i in range(1,num_terms+1):
    sum_series += multiple*i
print("The of the series is",sum_series)