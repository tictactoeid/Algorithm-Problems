# 플로이드
# 골드 4
import math
n = int(input())
m = int(input())

cost = [[math.inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    line = list(map(int, input().split()))
    cost[line[0]-1][line[1]-1] = min(cost[line[0]-1][line[1]-1], line[2])

for i in range(n):
    cost[i][i] = 0


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                cost[i][j] = 0
                continue

            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])


for i in range(n):
    for j in range(n):
        if math.isinf(cost[i][j]):
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()