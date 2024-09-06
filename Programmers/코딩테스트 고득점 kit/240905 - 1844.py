# 게임 맵 최단거리
# 레벨 2
# DFS / BFS

from collections import deque


def solution(maps):
    answer = 0
    q = deque()
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q.append((0, 0, 1))

    while q:
        i, j, dist = q.popleft()
        if i == len(maps) - 1 and j == len(maps[0]) - 1:
            return dist

        visited[i][j] = True
        neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for x in neighbors:
            if 0 <= x[0] < len(maps) and 0 <= x[1] < len(maps[0]):
                if not visited[x[0]][x[1]] and maps[x[0]][x[1]]:
                    visited[x[0]][x[1]] = True
                    q.append((x[0], x[1], dist + 1))

    return -1