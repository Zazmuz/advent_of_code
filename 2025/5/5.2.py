with open("5.txt", "r") as file:
    lines = file.readlines()

ranges = []

for line in lines:
    if line.strip() == "":break

    a,b = line.strip().split('-')
    a = int(a)
    b = int(b)
    ranges.append((a, 1))
    ranges.append((b, 0))

ranges.sort()
f = 0
last = None
on = 0
for event in ranges:
    if event[1]:
        if not on:
            last = event[0]
        on += 1
    else:
        on -= 1
        if not on:
            f += event[0] - last + 1
            print(f"{last}-{event[0]}")
print(f)