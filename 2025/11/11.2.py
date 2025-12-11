from collections import defaultdict, deque
with open("11.txt", "r") as file:
    lines = file.readlines()

edges = defaultdict(list)
for line in lines:
    f, t = line.strip().split(": ")

    for to in t.split():
        edges[f].append(to)

dp = {}
def dfs(node, fft=False, dac=False):
    if node == "out":
        return fft and dac
    if (node, fft, dac) in dp:
        return dp[(node, fft, dac)]

    ret = 0
    for neighbor in edges[node]:
        ret += dfs(neighbor, fft or neighbor == "fft", dac or neighbor == "dac")
    
    dp[(node, fft, dac)] = ret
    return ret

print(dfs("svr"))