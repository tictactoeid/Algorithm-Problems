# N과 M (8)
# 실버 3

n, m = map(int, input().split())
line = list(map(int, input().split()))
line.sort()


def dfs(i, visited): #백트래킹
    visited.append(line[i])
    if len(visited) == m:
        for j in visited:
            print(j, end=' ')
        print()
        return

    for next in range(i, n):
        dfs(next, visited)
        visited.remove(line[next])

for i in range(n):
    dfs(i, [])