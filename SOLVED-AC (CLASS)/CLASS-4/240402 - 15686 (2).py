# 치킨 배달
# 골드 5
# (2) backtracking

from itertools import combinations
import math

n, m = map(int, input().split())
#mat = [[] for _ in range(n)]
houses = []
chickens = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 2:
            chickens.append((i, j))
        elif line[j] == 1:
            houses.append((i, j))

dist = [math.inf for _ in range(len(houses))]
result = math.inf
visited = [False for _ in range(len(chickens))]
# 치킨집이 얼마 안 되기 때문에, set() 등으로 하는 것보다 그냥 list로 하는 게 시간을 줄일 수 있다.
def backtracking(idx, cnt):
    # 그리고 선택한 치킨집을 array 등으로 넘겨주는 것보다, 그냥 cnt만 하는 게 빠르고,
    # idx를 받아서 지금까지 방문한 치킨집은 재방문하지 않는 게 빠르다

    global result
    if cnt == m:
        dist = [math.inf for _ in range(len(houses))]
        for c in range(len(chickens)):
            if not visited[c]:
                continue
            for i in range(len(houses)):
                dist[i] = min(dist[i], abs(chickens[c][0] - houses[i][0]) + abs(chickens[c][1] - houses[i][1]))
        result = min(result, sum(dist))
        return

    for candidate in range(idx, len(chickens)):
        if visited[candidate]:
            continue
        #backtracking(chick + [candidate])
        #chick.add(candidate)
        visited[candidate] = True
        backtracking(candidate + 1, cnt + 1)
        visited[candidate] = False


backtracking(0, 0)
print(result)