with open("input.txt", "r") as f:
    input = f.read().splitlines()

arr = []
for o in input[0]:
    arr.append(0)
for a in input:
    b=0
    for i in a:
        if i == "1":
            arr[b] += 1
        else:
            arr[b] -= 1
        b += 1
gamma=''
epsilon=''
for j in arr:
    if j > 1:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
print(int(gamma,2)*int(epsilon,2))