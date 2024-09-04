# 아이템 줍기
# 레벨 3
# DFS / BFS

from collections import deque

#n = 50
n = 9


def bfs_reach(mat, i, j):
    if i == 0 or i == n-1 or j == 0 or j == n-1:
        return True

    q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]

    q.append((i, j))
    while q:
        i, j = q.popleft()
        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
        for ne in neighbors:
            if ne[0] < 0 or ne[0] > n-1 or ne[1] < 0 or ne[1] > n-1:
                continue
            if not visited[ne[0]][ne[1]] and not mat[ne[0]][ne[1]]:
                if ne[0] == 0 or ne[0] == n-1 or ne[1] == 0 or ne[1] == n-1:
                    return True

                q.append(ne)
                visited[ne[0]][ne[1]] = True
    return False


def reachable(mat, i, j):
    if i < 0 or i > n-1 or j < 0 or j > n-1:
        return False
    if not mat[i][j]:
        return False
    if i == 0 or i == n-1 or j == 0 or j == n-1:
        return True

    # # 안쪽에 빈 공간 있는 경우 처리 불가.
    # neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    # for neighbor in neighbors:
    #     if not mat[neighbor[0]][neighbor[1]]:  # border
    #         return True
    return bfs_reach(mat, i, j)


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    characterX -= 1
    characterY -= 1
    itemX -= 1
    itemY -= 1

    # TODO: mat[i][j]가 (i,j)가 길 위인지를 판단하는게 아니라, i->i+1로 가는 path가 있는지를 판단하는 식으로 바꾸어야 함

    mat = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for rec in rectangle:
        x1 = rec[0] - 1
        y1 = rec[1] - 1
        x2 = rec[2] - 1
        y2 = rec[3] - 1

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                mat[i][j] = 1

    # TODO: bfs here.

    q = deque()
    visited_ = [[False for _ in range(n)] for _ in range(n)]
    q.append((characterX, characterY, 0))  # (x, y, distance)
    visited_[characterX][characterY] = True

    while q:
        x, y, dist = q.popleft()
        if x == itemX and y == itemY:
            return dist
        visited_[x][y] = True
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for ne in neighbors:
            #print(ne)
            if 0 <= ne[0] < n and 0 <= ne[1] < n:
                #print(ne)
                if not visited_[ne[0]][ne[1]] and reachable(mat, ne[0], ne[1]):
                    if ne[0] == itemX and ne[1] == itemY:
                        for i in range(n):
                            print(mat[i])
                        print()
                        for i in range(n):
                            print(visited_[i])
                        return dist + 1

                    q.append((ne[0], ne[1], dist + 1))


    # return answer
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
