# N과 M(2)
# 실버 3

n, m = map(int, input().split())
visited = []

def dfs(num, visited):
    if num not in visited:
        visited.append(num)
    if len(visited) == m:
        for i in visited:
            print(i, end=' ')
        print()
        return
    for i in range(num, n+1):
        if i not in visited:
            dfs(i, visited)
            visited.remove(i)

for i in range(1, n+1):
    dfs(i, [])