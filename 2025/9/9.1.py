with open("9.txt", "r") as file:
    lines = file.readlines()

coords = []

for pos in lines:
    x, y = map(int, pos.split(","))
    coords.append((x, y))

m = 0

for coord1 in coords:
    for coord2 in coords:
        if coord1 != coord2:
            x1, y1 = coord1
            x2, y2 = coord2
            dist = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            m = max(m, dist)
print(m)