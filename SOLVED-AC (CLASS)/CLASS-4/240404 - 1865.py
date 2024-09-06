# 웜홀
# 골드 3

import sys
import math

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    nodes = [10001 for _ in range(n)]
    # 여기서 math.inf를 쓰면
    # negative weight에 의해 inf는 갱신되지 않는데
    # 시작점과 연결되지 않은 node는 계속 inf가 된다.
    # 이 문제는 시작점이 고정된 문제가 아니고, 전체 graph에 neg-cycle이 존재하는지
    # 묻고 있으므로, inf가 아닌 적당히 큰 값을 넣어
    # 시작점과 연결되지 않은 node라도 n+1번째 iterate에서 계속 갱신되도록 해야 한다

    roads = [[0, 0, 0] for _ in range(m)]
    wormholes = [[0, 0, 0] for _ in range(w)]

    for i in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        roads[i][0] = s - 1
        roads[i][1] = e - 1
        roads[i][2] = t

    for i in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        wormholes[i][0] = s - 1
        wormholes[i][1] = e - 1
        wormholes[i][2] = t

    # Bellman - Ford
    def relax(edge, isRoad = True):
        start = edge[0]
        end = edge[1]
        weight = edge[2]
        if isRoad:
            nodes[end] = min(nodes[end], nodes[start] + weight)
            nodes[start] = min(nodes[start], nodes[end] + weight)
        else:
            nodes[end] = min(nodes[end], nodes[start] - weight)


    nodes[0] = 0
    for _ in range(n):
        for edge in roads:
            relax(edge, True)
        for edge in wormholes:
            relax(edge, False)
    # 이후 갱신된다면 neg-cycle이 존재!
    flag = False
    for edge in wormholes:
        start = edge[0]
        end = edge[1]
        weight = edge[2] * -1
        if nodes[end] > nodes[start] + weight:
            flag = True
            break
    if not flag:
        for edge in roads:
            start = edge[0]
            end = edge[1]
            weight = edge[2]
            if nodes[end] > nodes[start] + weight:
                flag = True
                break
            if nodes[start] > nodes[end] + weight:
                flag = True
                break
    if flag:
        print("YES")
    else:
        print("NO")





