# ABCDE
# 골드 5
import sys
n, m = map(int, input().split())

friend = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
    #friend[a][b] = True
    #friend[b][a] = True

#print(friend)
def backtracking(node, start, visited, depth):
    #print(start, node, depth)
    if depth == 4:
        return True

    flag = False
    for f in friend[node]:
        if f in visited:
            continue
        if backtracking(f, start, visited + [f], depth + 1):
            flag = True
            break
    return flag


for i in range(n):
    if backtracking(i, i, [i], 0):
        print(1)
        sys.exit()

print(0)

