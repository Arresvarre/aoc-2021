count = 0
with open("input.txt", "r") as f:
    a = f.read().splitlines()

pre = a[0]
for i in a:
    if int(i) > int(pre):
        count += 1
        pre = i
    else:
        pre = i

print(count)