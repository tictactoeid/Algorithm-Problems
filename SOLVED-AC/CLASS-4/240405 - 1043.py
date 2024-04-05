# 거짓말
# 골드 4
import sys
n, m = map(int, input().split())

parent = [x for x in range(n+1)]
truth = list(map(int, input().split()))
t = truth.pop(0)
for tr in truth:
    parent[tr] = truth[0]

def find(i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent[i])
        return parent[i]


def union(i, j):
    root_i = find(i)
    root_j = find(j)

    if root_i != root_j:
        parent[root_j] = root_i


if t == 0:
    print(m)
    sys.exit()

parties = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

for party in parties:
    #root_tr = find(truth[0])
    for i in range(len(party)):
        if i < 2:
            continue
        union(party[1], party[i])

for party in parties:
    if find(party[1]) != find(truth[0]):
        cnt += 1

print(cnt)




