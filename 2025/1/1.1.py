with open("1.txt") as f:
    data = f.readlines()

s = 0

point = 50
for line in data:
    d, n = line[0], int(line[1:])
    if d == 'L':
        n = -n

    point = (point + n) % 100

    if point == 0:
        s += 1

if point == 0:
    s += 1
print(s)