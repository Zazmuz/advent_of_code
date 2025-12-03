with open("3.txt") as f:
    data = f.readlines()

s = 0

for line in data:
    line = line.strip()
    line = line[::-1]
    small = line[0]
    large = line[1]
    for c in line[2:]:
        if c >= large:
            if large > small:
                small = large
            large = c
    s += int(large + small)
print(s)