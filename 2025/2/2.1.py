with open("2.txt") as f:
    data = f.read().strip().split(',')

c = 0

for line in data:
    s, e = map(int, line.split('-'))

    for i in range(s, e + 1):
        si = str(i)
        h = len(si) // 2
        if si[:h] == si[h:]:
            c += i
print(c)