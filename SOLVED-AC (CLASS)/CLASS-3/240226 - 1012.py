# 유기농 배추
# 실버 2

import sys
sys.setrecursionlimit(10**6)

t = int(input())

def getNeighbors(x, y):
    result = []
    if x > 0:
        result.append((x - 1, y))
    if x < m-1:
        result.append((x + 1, y))
    if y > 0:
        result.append((x, y - 1))
    if y < n-1:
        result.append((x, y + 1))

    return result


def unvisited():
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == -1:
                return i, j
    return False


def dfs(x, y, num):
    matrix[x][y] = num # visited = True

    for neighbor in getNeighbors(x, y):
        if matrix[neighbor[0]][neighbor[1]] < 0:
            dfs(neighbor[0], neighbor[1], num)



for _ in range(t):
    m, n, k = map(int, input().split())

    matrix = [[0 for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = -1

    count = 0
    while unvisited():
        count += 1
        x, y = unvisited()
        dfs(x, y, count)

    print(count)