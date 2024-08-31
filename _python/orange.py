n = int(input("Enter the of oranges:"))
oranges = []
for i in range(n):
    oranges.append(int(input(f"Enter the size of the {i+1} orange:")))
print("Oranges before sorting:",oranges)

def arrange_orange(n,list_O):
    j = 0
    pivot = list_O[-1]
    for i in range(n-1):
        if list_O[i] < pivot:
            list_O[j],list_O[i] = list_O[i],list_O[j]
            j += 1
    list_O[j],list_O[-1] = list_O[-1],list_O[j]


arrange_orange(n,oranges)
print("Oranges after sorting:",oranges)
