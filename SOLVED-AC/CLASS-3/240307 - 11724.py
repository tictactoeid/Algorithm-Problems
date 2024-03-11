# 연결 요소의 개수
# 실버 2

# TODO

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

adjacency = set()


for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    adjacency.add((u-1, v-1))
    adjacency.add((v-1, u-1))

visited = set()


def dfs(node):
    visited.add(node)
    for u in range(n):
        if (u not in visited) and ((u, node) in adjacency) and u != node:
            dfs(u)


count = 1
dfs(0)
#print(visited)
for v in range(n):
    if v not in visited:

        dfs(v)
        #print(visited)
        count += 1

print(count)
