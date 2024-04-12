# 녹색 옷 입은 애가 젤다지?
# 골드 4
import sys
import heapq
import math


def dijkstra(n, mat):
    i = 0
    j = 0
    q = []
    cost = [[math.inf for _ in range(n)] for _ in range(n)]
    heapq.heappush(q, (mat[i][j], i, j))
    cost[i][j] = mat[i][j]
    while q:
        weight, i, j = heapq.heappop(q)
        if weight > cost[i][j]:
            continue
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for ne in neighbors:
            if 0 <= ne[0] < n and 0 <= ne[1] < n:
                if cost[ne[0]][ne[1]] > cost[i][j] + mat[ne[0]][ne[1]]:
                    cost[ne[0]][ne[1]] = cost[i][j] + mat[ne[0]][ne[1]]
                    heapq.heappush(q, (cost[ne[0]][ne[1]], ne[0], ne[1]))
    return cost[n-1][n-1]



problem = 0
while True:
    problem += 1
    n = int(sys.stdin.readline())
    if n == 0:
        break

    mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    result = dijkstra(n, mat)
    print("Problem {0}: {1}".format(problem, result))