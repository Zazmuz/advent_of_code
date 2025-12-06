from functools import reduce
with open("6.txt", "r") as file:
    lines = file.readlines()

problems = [[] for _ in range(len(lines[0].strip().split()))]

for line in lines[:-1]:
    nums = line.strip().split()
    for i, num in enumerate(nums):
        problems[i].append(int(num))
s = 0
for i, problem in enumerate(problems):
    op = lines[-1].strip().split()[i]
    if op == "*":
        res = reduce(lambda x, y: x * y, problem)
    elif op == "+":
        res = sum(problem)
    s += res
print(s)