# 스타트 택시
# 골드 2

from collections import deque
import math
import sys

n, m, oil = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


def get_distance(i1, j1, i2, j2):
    # (i1, j1) -> (i2, j2)

    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((i1, j1, 0))
    visited[i1][j1] = True

    while q:
        i, j, dist = q.popleft()
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for ne in neighbors:
            x = ne[0]
            y = ne[1]
            if 0 <= x < n and 0 <= y < n:
                if x == i2 and y == j2:
                    return dist + 1

                if not visited[x][y] and mat[x][y]:
                    q.append((x, y, dist+1))
                    visited[x][y] = True
    return None


def get_closest_customer(i1, j1, customers: dict):
    if (i1, j1) in customers.keys():
        return i1, j1, 0

    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((i1, j1, 0))
    visited[i1][j1] = True

    min_dist = math.inf
    candidates = []

    while q:
        i, j, dist = q.popleft()
        if dist > min_dist:
            break
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for ne in neighbors:
            x = ne[0]
            y = ne[1]
            if 0 <= x < n and 0 <= y < n:
                if (x, y) in customers.keys():
                    min_dist = dist
                    candidates.append((x, y))

                if not visited[x][y] and mat[x][y]:
                    q.append((x, y, dist+1))
                    visited[x][y] = True
    if not candidates:
        return None
    customer = min(candidates)
    return customer[0], customer[1], min_dist + 1


tmp1, tmp2 = map(int, input().split())

car = (tmp1 - 1, tmp2 - 1)
customers = {}
for i in range(m):
    a, b, c, d = map(int, input().split())
    customers[(a-1, b-1)] = (c-1, d-1)

i, j = car
while customers:
    customer = get_closest_customer(i, j, customers)
    if customer is None:
        if customers:
            print(-1)
            sys.exit()
        else:
            break
    i, j, dist1 = customer  # 승객 탑승
    oil -= dist1
    if oil <= 0:
        print(-1)
        sys.exit()

    i2, j2 = customers[(i, j)]  # 목적지로 이동
    dist2 = get_distance(i, j, i2, j2)
    oil -= dist2
    if oil < 0:  # 도착과 동시에 0이 되는 경우는 성공
        print(-1)
        sys.exit()

    oil +=



