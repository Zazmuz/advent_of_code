with open("7.txt", "r") as file:
    lines = file.readlines()

from collections import deque
q = deque()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "S":
            q.append((x, y))
            break

s = 0
vis = set()
while q:
    x, y = q.popleft()
    if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines) or (x, y) in vis:
        continue
    vis.add((x, y))
    pos = lines[y][x]
    print(pos, x, y)
    if pos == "^":
        s += 1
        q.append((x - 1, y))
        q.append((x + 1, y))
    else:
        q.append((x, y + 1))
print(s)