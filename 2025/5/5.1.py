with open("5.txt", "r") as file:
    lines = file.readlines()

ranges = []

r = True
f = 0
for line in lines:
    if line.strip() == "":
        r = False
        continue
    if r:
        a,b = line.strip().split('-')
        a = int(a)
        b = int(b)
        ranges.append((a, b))
    else:
        a = int(line.strip())
        for start, end in ranges:
            if start <= a <= end:
                f += 1
                break
print(f)