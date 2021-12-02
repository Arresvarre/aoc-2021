with open("input.txt", "r") as f:
    a = f.read().splitlines()

depth = 0
hp = 0
aim = 0

for i in a:
    p = i.split(' ')
    print(p)
    if p[0] == "forward":
        hp += int(p[1])
        depth += aim * int(p[1])
    elif p[0] == "down":
        aim += int(p[1])
    elif p[0] == "up":
        aim -= int(p[1])

print(depth * hp)