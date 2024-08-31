"""  
# Linear Search:
def linear_search(students, search_name):
    for i in students.keys():
        if i == search_name:
            return i
    return -1

n = int(input('Enter input size: '))

students = {}
print(f'Enter the {n} students')
for i in range(n):
    id=int(input('Enter id:'))
    name=input('Enter name:')
    students[id]=name

print('The input data is \n', students)
search_name = int(input('Enter the search id: '))

index = linear_search(students, search_name)
if index == -1:
    print(f' id-{search_name} was not found in the dictionary')
else:
    print(f'{students[index]} was found in the dictionary.')

"""
""" 
#Binary Search:
 """
"""  
# insertion sort:
def insertion_sort(array_name):
    for i in range(1,len(array_name)):
        ele = array_name[i]
        j=i-1
        while j >= 0 and ele < array_name[j]:
            array_name[j+1] = array_name[j]
            j = j - 1
            array_name[j+1] = ele



array = []
n = int(input("Enter the size:"))
print("Enter the elements of the array:")
for i in range(n):
    array.append(int(input()))

print("The array before insertion sort",array)

insertion_sort(array)

print("The array after insertion sort",array)    

"""

""" 
# bubble sort:

array = []
n = int(input("Enter the size:"))
print("Enter the elements of the array:")
for i in range(n):
    array.append(int(input()))
print("Array elements before bubble sort:",array)
for i in range(n):
    sort = True
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            sort = False
    if sort :
        break
print("Array elements after bubble sort:",array)

 """

"""  
brakets = input("Enter paranthesis:")
count1= brakets.count("(")
count2 = brakets.count(")")

if count1 != count2 or count2 > count1:
    print("Improper arrangement.")
elif count2 == count1:
    print(f"{(count1+count2)/2} pairs.")

    """

"""  
og_num = input("Enter any 4 digit number:")
for i in og_num :
    if og_num.count(i) > 2:
        exit(f"{i} has repeated more than 2 times.")
a_num = sorted(list(og_num))
d_num = sorted(list(og_num),reverse = True)
a_s = [str(integer) for integer in a_num]
a_st = "".join(a_s)
d_s = [str(integer) for integer in d_num]
d__st = "".join(d_s)
d_int =int(d__st)
a_int = int(a_st)
diff = d_int - a_int
count = 0
while(True):
    a_num = sorted(list(diff))
    d_num = sorted(list(diff),reverse = True)
    a_s = [str(integer) for integer in a_num]
    a_st = "".join(a_s)
    d_s = [str(integer) for integer in d_num]
    d__st = "".join(d_s)
    d_int =int(d__st)
    a_int = int(a_st)
    diff1 = d_int - a_int
    if diff == diff1:
        break
    else:
        diff = diff1
    count += 1
    
    """

"""  
n = int(input("Enter numbers of boys or girls:"))
b = []
g = []
for i in range(n):
    b.append(float(input(f"Enter {i+1} boys height:")))
    g.append(float(input(f"Enter {i+1} girls height:")))
boys = sorted(b)
girls = sorted(g)
res = []
for i in range(n):
    for j in range(n):
        if j%2 != 0:
            res.append(boys[i])
        else:
            res.append(girls[i])
res_sort = sorted(res)
print(res)
if res == res_sort:
    print("YES")
else:
    print("NO")

"""
  

