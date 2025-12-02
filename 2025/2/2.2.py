with open("2.txt") as f:
    data = f.read().strip().split(',')

c = 0

for line in data:
    s, e = map(int, line.split('-'))

    for i in range(s, e + 1):
        si = str(i)

        if any(all(si[j*len(si) // h:(j+1)*len(si) // h] == si[:len(si) // h] for j in range(h)) for h in range(2, len(si) + 1)):
            c += i

print(c)