# 여행 가자
# 골드 4
# union-find
import sys

n = int(input())
m = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

for i in range(m):
    plan[i] -= 1

parent = [i for i in range(n)]


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = parent[parent[x]]
        return find(parent[x])


def union(x, y):
    p1 = find(x)
    p2 = find(y)
    if p1 == p2:
        return
    elif p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2


for i in range(n):
    for j in range(n):
        if mat[i][j]:
            union(i, j)

for i in range(m-1):
    if find(plan[i]) != find(plan[i+1]):
        print("NO")
        sys.exit()

print("YES")
