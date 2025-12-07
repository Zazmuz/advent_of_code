with open("7.txt", "r") as file:
    lines = file.readlines()

mem = {}
def dp(x, y):
    if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
        return 0
    if (x, y) in mem:
        return mem[(x, y)]

    pos = lines[y][x]
    ret = 0

    if pos == "^":
        ret += 1 + dp(x - 1, y) + dp(x + 1, y)
    else:
        ret += dp(x, y + 1)
    
    mem[(x, y)] = ret
    return ret

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "S":
            print(1 + dp(x, y))
            break
    else:
        continue
    break