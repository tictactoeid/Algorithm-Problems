# 돌 그룹
# 골드 4
# 재활훈련: bfs

from collections import deque

a, b, c = map(int, input().split())


def bfs(a, b, c):
    if a == b and b == c:
        return 1

    rocks = sorted([a, b, c])
    visited = set()

    q = deque()
    q.append(rocks)
    visited.add(tuple(rocks))

    while q:
        rocks = q.popleft()
        if rocks[0] == rocks[1] and rocks[1] == rocks[2]:
            return 1

        visited.add(tuple(rocks))

        a = rocks[0]
        b = rocks[1]
        c = rocks[2]

        if a < b:
            new = sorted([a+a, b-a, c])
            if tuple(new) not in visited:
                q.append(new)
        if b < c:
            new = sorted([a, b+b, c-b])
            if tuple(new) not in visited:
                q.append(new)
        if a < c:
            new = sorted([a+a, b, c-a])
            if tuple(new) not in visited:
                q.append(new)
    return 0

print(bfs(a, b, c))