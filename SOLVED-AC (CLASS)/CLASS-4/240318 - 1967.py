# 트리의 지름
# 골드 4

# leaf-to-leaf DFS
import sys
n = int(input())
edges = {}
neighbors = [[] for _ in range(n)]
non_leaves = set()

for i in range(n-1):
    parent, child, cost = map(int, sys.stdin.readline().split())
    parent -= 1
    child -= 1
    edges[(parent, child)] = cost
    edges[(child, parent)] = cost
    non_leaves.add(parent)
    neighbors[parent].append(child)
    neighbors[child].append(parent)

leaves = set(i for i in range(n)).difference(non_leaves)


def dfs(node, visited, cost):
    visited.add(node)
    max_cost = cost
    for neighbor in neighbors[node]:
        if neighbor not in visited:
            max_cost = max(max_cost, dfs(neighbor, visited, cost + edges[(node, neighbor)]))

    return max_cost



result = 0
for leaf in leaves:
    result = max(result, dfs(leaf, set(), 0))
print(result)
