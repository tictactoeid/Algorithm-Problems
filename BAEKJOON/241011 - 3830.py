# 교수님은 기다리지 않는다
# 플래티넘 3

import sys
sys.setrecursionlimit(10**5)

def find(x):
    global parents
    if parents[x][0] == x:
        return [x, 0]
    root = find(parents[x][0])[0]
    p = parents[x][0]
    parents[x][1] += parents[p][1]
    parents[x][0] = root
    return parents[x]


def union(a, b, w):
    global parents
    p1 = find(a)
    p2 = find(b)

    if p1[0] == p2[0]:
        return
    #elif p1[0] > p2[0]:

    parents[p2[0]] = [p1[0], p1[1] + w - p2[1]]


while True:
    n, m = map(int, sys.stdin.readline().split())
    if not n and not m:
        break

    parents = [[i, 0] for i in range(n)]

    for _ in range(m):
        work = list(sys.stdin.readline().split())
        if work[0] == "!":
            a, b, w = map(int, work[1:])
            union(a-1, b-1, w)
        else:
            a, b = map(int, work[1:])
            p1 = find(a-1)
            p2 = find(b-1)
            if p1[0] == p2[0]:
                print(p2[1] - p1[1])
            else:
                print("UNKNOWN")

