# 이분 그래프
# 골드 4

from collections import deque

k = int(input())


def is_bipartite(v, edges):
    colors = [None for _ in range(v)]
    RED = -1
    BLUE = +1

    node = 0
    q = deque()

    while True:  # 비연결 그래프를 고려해야 하는가? -> 해야 함

        q.append(node)
        colors[node] = RED

        while q:
            node = q.popleft()
            for next in edges[node]:
                if colors[next] is None:
                    q.append(next)
                    colors[next] = -colors[node]
                else:
                    if colors[next] == colors[node]:
                        return "NO"

        try:
            node = colors.index(None)
        except ValueError:
            break
    return "YES"


for _ in range(k):
    v, e = map(int, input().split())
    edges = [[] for _ in range(v)]
    for _ in range(e):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        edges[x].append(y)
        edges[y].append(x)
    print(is_bipartite(v, edges))
