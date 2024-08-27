numofreq = int(input("Enter the number of requests:"))
requests = []
for i in range(numofreq):
    requests.append(int(input(f"Enter the {i+1} requests for allocation/deallocating:")))

server1 = [requests[0]]
for i in range(1,numofreq):
    if i%2 == 0:
        server1.append(requests[i])
Sum =sum(server1)
if sum(server1) > 0:
    print(f"server 1 : delocated {Sum} units of memeory.")
else:
    print(f"server 1 : allocated {Sum} units of memeory.")