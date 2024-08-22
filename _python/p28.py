#Program statement:Print Prime numbers between M and N(M < N)

start_num = int(input("Enter the starting range:"))
end_num = int(input("Enter the ending range(>Starting range):"))
prime = [2,3,5]
prime_r = []
if end_num <= start_num :
    exit("INVALID INPUT!!!")
if end_num in prime:
    for i in range(start_num,end_num+1):
        print("The prime numbers between",start_num,"and",end_num,"are",prime[i])
else:
    for i in range(start_num,end_num+1):
        if i %2 != 0 and i%3 != 0 and i%5 != 0 :
            #print(i,end=" ")
            prime_r.append(i)
print("The prime numbers between",start_num,"and",end_num,"are")
for i in prime_r:
    print(i,end=" ")
