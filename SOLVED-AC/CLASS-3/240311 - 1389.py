# 케빈 베이컨의 6단계 법칙
# 실버 1
import math

n, m = map(int, input().split())

distance = [[math.inf for _ in range(n)] for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    distance[i - 1][j - 1] = 1
    distance[j - 1][i - 1] = 1

for i in range(n):
    distance[i][i] = 1

# Floyd - Warshall

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
            else:
                distance[i][j] = 0

kevin_bacon = [(0, 0) for _ in range(n)]
for i in range(n):
    kevin_bacon[i] = (i, sum(distance[i]))

#print(distance)
#print(kevin_bacon)
kevin_bacon.sort(key=lambda x: (x[1], x[0]))
print(kevin_bacon[0][0] + 1)
