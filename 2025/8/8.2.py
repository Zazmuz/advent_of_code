import sys

sys.setrecursionlimit(200000)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i

            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.num_sets -= 1
            return True
        return False

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])

    dsu = DSU(n)
    mst_weight = 0
    edges_count = 0

    for u, v, weight, ps1, ps2 in edges:
        if dsu.union(u, v):
            mst_weight += weight
            edges_count += 1
            if edges_count == n - 1:
                return ps1[0] * ps2[0]

    if edges_count != n - 1:
        return -1

    return mst_weight

with open("8.txt", "r") as file:
    lines = file.readlines()

coords = []

for pos in lines:
    x, y, z = map(int, pos.split(","))
    coords.append((x, y, z))

n = len(coords)
edges = []

for i in range(n):
    for j in range(i+1, n):
        x1, y1, z1 = coords[i]
        x2, y2, z2 = coords[j]
        dist = abs(x1 - x2)**2 + abs(y1 - y2)**2 + abs(z1 - z2)**2
        dist = dist**0.5
        edges.append((i, j, dist, (x1, y1, z1), (x2, y2, z2)))


print(kruskal(n, edges))