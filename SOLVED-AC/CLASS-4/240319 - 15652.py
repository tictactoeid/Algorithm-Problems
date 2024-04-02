# N과 M (4)
# 실버 3


n, m = map(int, input().split())

def dfs(num, visited): #백트래킹
    visited.append(num)

    if len(visited) == m:
        for i in visited:
            print(i, end=' ')
        print()
        return

    for i in range(num, n+1):
        dfs(i, visited)
        visited.remove(i)


for i in range(1, n+1):
    dfs(i, [])
