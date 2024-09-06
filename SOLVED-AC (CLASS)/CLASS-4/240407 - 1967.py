# 트리의 지름
# 골드 5

import sys
n = int(sys.stdin.readline())

if n == 1:
    print(0)
    sys.exit()

edges = [[] for _ in range(n)]
paths = [0 for _ in range(n)]  # from root to node i
parents = [-1 for _ in range(n)]

leaf = 0  # start no. of leaf nodes

for _ in range(n-1):
    start, end, weight = map(int, sys.stdin.readline().split())
    start -= 1
    end -= 1
    edges[start].append([end, weight])
    parents[end] = start

leaf = start + 1


def path(node):
    if node >= leaf:
        # leaf node
        return

    for edge in edges[node]:
        child = edge[0]
        weight = edge[1]
        paths[child] = paths[node] + weight
        path(child)






path(0)
print(paths)

result = 0
for i in range(leaf, n):
    for j in range(i+1, n):
        result = max(result, paths[i] + paths[j])
print(result)