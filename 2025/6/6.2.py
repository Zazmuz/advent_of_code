from functools import reduce
with open("6.txt", "r") as file:
    lines = file.readlines()

problems = [[] for _ in range(len(lines[0].strip().split()))]
pr = len(problems) - 1
for i in range(len(lines[0].strip()), -1, -1):
    n = ""
    for j in range(len(lines)):
        p = lines[j][i]
        if p.isnumeric():
            n += p
        elif p in ("+*"):
            problems[pr].append(int(n))
            n = ""
            pr -= 1
    if n != "":
        problems[pr].append(int(n))

print(problems)

s = 0
for i, problem in enumerate(problems):
    op = lines[-1].strip().split()[i]
    if op == "*":
        res = reduce(lambda x, y: x * y, problem)
    elif op == "+":
        res = sum(problem)
    s += res
print(s)