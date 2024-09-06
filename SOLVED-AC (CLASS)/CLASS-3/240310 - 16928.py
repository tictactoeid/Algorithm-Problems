# 뱀과 사다리 게임
# 골드 5

from collections import deque
import sys


# 그냥 bfs인줄 알았으나 생각보다 요구사항이 많은 문제

n, m = map(int, sys.stdin.readline().split())

edges = [0 for _ in range(101)]

for _ in range(n+m):
    u, v = map(int, sys.stdin.readline().split())
    edges[u] = v

q = deque()
visited = set()

depth = 0
q.append((1, depth))
found = False

while len(q) > 0:
    node, depth = q.popleft()
    visited.add(node)
    if node == 100:
        print(depth)
        break

    if 1 <= node <= 100 and edges[node] != 0:
        node = edges[node]
        if node not in visited: # 체크안하면 시간초과
            q.appendleft((node, depth))
            visited.add(node)
            if node == 100:
                print(depth)
                found = True
                break


        # 사다리나 뱀은 강제로 타야 함.

    for i in range(node + 1, node + 7):
        if i not in visited:
            q.append((i, depth + 1))
