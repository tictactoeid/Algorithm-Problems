# 치킨 배달
# 골드 5
# (1) itertools

from itertools import combinations
import math

n, m = map(int, input().split())
mat = [[] for _ in range(n)]
houses = []
chickens = []

for i in range(n):
    mat[i] = list(map(int, input().split()))
    for j in range(n):
        if mat[i][j] == 2:
            chickens.append((i, j))
        elif mat[i][j] == 1:
            houses.append((i, j))

dist = [math.inf for _ in range(len(houses))]
result = math.inf

for chick in combinations(chickens, m):
    dist = [math.inf for _ in range(len(houses))]
    for c in chick:
        for i in range(len(houses)):
            dist[i] = min(dist[i], abs(c[0] - houses[i][0]) + abs(c[1] - houses[i][1]))
    result = min(result, sum(dist))

print(result)