# 벽 부수고 이동하기
# 골드 3

from collections import deque
import sys

n, m = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(n)]

q = deque()

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
visited[0][0][0] = True # not broken
visited[1][0][0] = True # broken

# visited를 1개만 쓰는 경우
# 특정 지점에 broken이 not broken보다 먼저 도착하면
# visited 처리되어 not broken은 해당 지점으로 갈 수 없게 되고
# 이로 인해 아직 벽을 부술 기회가 남아있는 not broken은
# 가능한 path를 찾지 못하는 경우가 생김

q.append((0, 0, False, 1))

# (r, c, has_broken_wall, distance)
# distance includes start and end points

while q:
    r, c, broken, dist = q.popleft()

    if (r, c) == (n-1, m-1):
        print(dist)
        sys.exit()

    neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

    for x, y in neighbors:
        if 0 <= x < n and 0 <= y < m:
            if broken:
                if not visited[1][x][y]:
                    if mat[x][y] == 0:
                        visited[1][x][y] = True
                        q.append((x, y, True, dist+1))
            else:
                if not visited[0][x][y]:
                    if mat[x][y] == 0:
                        visited[0][x][y] = True
                        visited[1][x][y] = True
                        q.append((x, y, False, dist+1))
                    else:
                        visited[1][x][y] = True
                        q.append((x, y, True, dist+1))


print(-1)
