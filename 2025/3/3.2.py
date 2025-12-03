with open("3.txt") as f:
    data = f.readlines()

s = 0

def cR(b, i, c):
    if i == -1:
        return

    if c >= b[i]:
        cR(b, i - 1, b[i])
        b[i] = int(c)
    

for line in data:
    line = line.strip()
    line = line[::-1]

    big = [int(c) for c in line[:12]]

    for c in line[12:]:
        cR(big, 11, int(c))
    big = big[::-1]
    s += int(''.join(str(c) for c in big))
print(s)