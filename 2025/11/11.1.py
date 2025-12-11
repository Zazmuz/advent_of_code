from collections import defaultdict, deque
with open("11.txt", "r") as file:
    lines = file.readlines()

edges = defaultdict(list)
for line in lines:
    f, t = line.strip().split(": ")

    for to in t.split():
        edges[f].append(to)

q = deque()
q.append(("you", ()))

visited = set()

s = 0
while q:
    node, path = q.popleft()
    print(node, path)
    if node == "out":
        s += 1

    if (node, path) in visited:
        continue

    visited.add((node, path))

    for neighbor in edges[node]:
        q.append((neighbor, path + (node,)))
print(s)