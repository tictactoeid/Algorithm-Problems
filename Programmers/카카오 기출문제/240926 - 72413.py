# 합승 택시 요금
# 레벨 3
# 2021 KAKAO BLIND RECRUITMENT

# Floyd-Warshall 후
# 임의의 합승 도착 지점 C에 대하여
# S -> C + C -> A + C -> B의 요금

import math


def solution(n, s, a, b, fares):
    s -= 1
    a -= 1
    b -= 1

    dist = [[math.inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for fare in fares:
        x, y, w = fare
        dist[x-1][y-1] = w
        dist[y-1][x-1] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

    answer = min(dist[s][c] + dist[c][a] + dist[c][b] for c in range(n))

    return answer
