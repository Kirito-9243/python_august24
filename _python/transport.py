n = int(input("Enter the size of 1st list:"))
m = int(input("Enter the size of 2nd list:"))
list_1 = []
list_2 = []
missing = []
if m > n :
    exit("Size of the 2nd list must be <= size of the 1st.")
else:
    for i in range(n):
        list_1.append(int(input(f"Enter the {i+1} element in list-1:")))
    for i in range(m):
        list_2.append(int(input(f"Enter the {i+1} element in list-2:")))

list_1s = sorted(list_1)
list_2s = sorted(list_2)

j = 0
if m == 0:
    missing.append(list_1s)
else:
    for i in range(n):
        if list_1s[i] == list_2s[j]:
            j += 1
        else:
            missing.append(list_1s[i])
        if j == m and i != n-1:
            missing.extend(list_1s[i+1:])
            break    
print("The missing elements are:",missing)