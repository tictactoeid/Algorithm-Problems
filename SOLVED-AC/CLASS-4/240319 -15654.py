# N과 M (5)
# 실버 3

n, m = map(int, input().split())
line = list(map(int, input().split()))
line.sort()


def dfs(i, visited):
    if line[i] not in visited:
        visited.append(line[i])
    if len(visited) == m:
        for j in visited:
            print(j, end=' ')
        print()
        return
    for next in range(n):
        if line[next] not in visited:
            dfs(next, visited)
            visited.remove(line[next])


for i in range(n):
    dfs(i, [])
