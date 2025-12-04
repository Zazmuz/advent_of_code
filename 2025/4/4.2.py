with open("4.txt", "r") as file:
    lines = file.readlines()

grid = []

for line in lines:
    line = line.strip()
    row = list(line)
    grid.append(row)

def inside(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def nei(x, y):
    diffs = [-1, 0, 1]
    directions = [(i, j) for i in diffs for j in diffs if not (i == 0 == j)]

    s = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if inside(nx, ny) and grid[nx][ny] == "@":
            s += 1
    return s

t = 0
while True:
    c = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@" and nei(i, j) < 4:
                grid[i][j] = "."
                c += 1
    if c == 0:
        break
    t += c
    
print(t)