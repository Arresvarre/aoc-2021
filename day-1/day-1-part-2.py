with open("input.txt", "r") as f:
    a = f.read().splitlines()

newList = []
count = 0

for i in range(len(a)):
    if i == (len(a) - 2):
        break
    sum = int(a[i]) + int(a[i+1]) + int(a[i+2])
    newList.append(sum)

pre = newList[0]
for i in newList:
    if int(i) > int(pre):
        count += 1
        pre = i
    else:
        pre = i

print(count)



