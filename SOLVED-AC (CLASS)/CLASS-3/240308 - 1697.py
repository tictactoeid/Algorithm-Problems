# 숨바꼭질
# 실버 1

from collections import deque

n, k = map(int, input().split())

if n >= k:
    print(n-k)

else:
    q = deque()
    visited = set()
    depth = 0
    visited.add(n)
    q.append((n, depth))

    while len(q) > 0:
        node, depth = q.popleft()
        if node == k:
            print(depth)
            break

        visited.add(node)

        adjs = [node-1, node+1]
        if node * 2 <= k * 2:
            adjs.append(node * 2)

        for adj in adjs:
            if adj not in visited:
                visited.add(adj)
                q.append((adj, depth+1))

