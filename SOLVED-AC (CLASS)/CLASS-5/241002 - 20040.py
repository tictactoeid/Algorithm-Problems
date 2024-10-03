# 사이클 게임
# 골드 4

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

lines = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

parents = [i for i in range(n)]


def find(x):
    if parents[x] == x:
        return x
    else:
        parent = parents[x]
        parents[x] = find(parent)
        return parents[x]


def union(x, y):
    p1 = find(x)
    p2 = find(y)
    if p1 == p2:
        return
    parents[p2] = p1


for i in range(m):
    x, y = lines[i]
    p1 = find(x)
    p2 = find(y)
    if p1 == p2:
        print(i+1)
        sys.exit()
    union(p1, p2)

print(0)



