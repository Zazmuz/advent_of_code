with open("sample.txt", "r") as file:
    lines = file.readlines()

buttons = []
for line in lines:
    a, *rest = line.strip().split(" ")
    toggles, joltage = rest[:-1], rest[-1]

    a = a[1:][:-1].replace("#", "1").replace(".", "0")
    size = len(a)
    a = int(a, 2)
    flips = []
    for toggle in toggles:
        toggle = toggle[1:][:-1].split(",")
        changes = 0
        for bitflipIndex in toggle:
            changes |= 1 << (int(bitflipIndex))
        flips.append(changes)
    buttons.append((a, flips, size))


def dp(goal, state, used, flipList):
    print(bin(state), used)
    if state == 0:
        return used
    if used >= 3:
        return 99999999999999

    res = 99999999999999

    for i in range(len(flipList)):
        newState = state ^ flipList[i]
        res = min(res, dp(goal, newState, used + 1, flipList))
    return res


s = 0
for but in buttons:
    a, flips, size = but
    state = (1 << (size)) - 1
    s = dp(a, state, 0, flips)
    print(s)