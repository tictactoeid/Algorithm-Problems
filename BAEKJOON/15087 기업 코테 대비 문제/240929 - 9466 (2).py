# 텀 프로젝트
# 골드 3

import sys
sys.setrecursionlimit(10**5)


def dfs(x):
    global cnt
    visited[x] = True
    current_team.append(x)
    next = students[x-1]

    if visited[next]:
        if next in current_team:
            idx = current_team.index(next)
            cnt += len(current_team[idx:])
        return
    else:
        dfs(next)


t = int(input())
for _ in range(t):
    n = int(input())
    students = list(map(int, input().split()))
    cnt = 0
    visited = [False for _ in range(n+1)]
    visited[0] = True
    for i in range(1, n+1):
        if not visited[i]:
            current_team = []
            dfs(i)
    print(n-cnt)
