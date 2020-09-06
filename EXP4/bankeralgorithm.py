p = int(input(" Give number of processes -> "))
r = int(input("Give number of resources -> "))
max_r = [int(i) for i in input("Give the maximum available for each resources ->").split()]

print("\nGive the already allocated resources for each process")
c_allocation = [[int(i) for i in input(f"Process <{j + 1}> -> ").split()] for j in range(p)]

print("\nGive the maximum resources for each process")
max_n = [[int(i) for i in input(f"Process <{j + 1}> : ").split()] for j in range(p)]

allocated = [0] * r
for i in range(p):
    for j in range(r):
        allocated[j] += c_allocation[i][j]
print(f"\ntotal allocated resources : {allocated}")

available = [max_r[i] - allocated[i] for i in range(r)]
for num in available: 
    if num < 0:
        print("The allocation is more than the given number of resources")
        exit(0)
print(f"total available resources : {available}\n")

running = [True] * p
c = p
while c != 0:
    s = False
    for i in range(p):
        if running[i]:
            executing = True
            for j in range(r):
                if max_n[i][j] - c_allocation[i][j] > available[j]:
                    executing = False
                    break
            if executing:
                print(f"Process {i + 1} is executing")
                running[i] = False
                c -= 1
                s = True
                for j in range(r):
                    available[j] += c_allocation[i][j]
                break
    if not s:
        print("It in unsafe state")
        break

    print(f"Its in safe state\nAvailable resources -> {available}\n")
