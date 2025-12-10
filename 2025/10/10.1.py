with open("10.txt", "r") as file:
    lines = file.readlines()

# convert to num
buttons = []
for line in lines:
    a, *rest = line.strip().split(" ")
    toggles, joltage = rest[:-1], rest[-1]

    a = a[1:][:-1].replace("#", "0").replace(".", "1")
    size = len(a)
    a = int(a[::-1], 2)
    flips = []
    for toggle in toggles:
        toggle = toggle[1:][:-1].split(",")
        changes = 0
        for bitflipIndex in toggle:
            changes |= 1 << (int(bitflipIndex))
        flips.append(changes)
    buttons.append((a, flips, size))
#

def dp(goal, state, used, idx, flipList):
    if state == goal:
        return used
    elif idx >= len(flipList):
        return 99999999999999

    res = 99999999999999

    newState = state ^ flipList[idx]
    res = min(res, dp(goal, state, used, idx+1, flipList), dp(goal, newState, used+1, idx+1, flipList))
    return res

s = 0
for but in buttons:
    a, flips, size = but
    state = (1 << (size)) - 1
    s += dp(a, state, 0, 0, flips)
print(s)