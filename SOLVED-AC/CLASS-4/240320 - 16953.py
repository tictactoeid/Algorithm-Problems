# A -> B
# 실버 2
from collections import deque


a, b = map(int, input().split())

q = deque()
depth = 1
node = a
q.append((node, depth))
visited = set()

while len(q) > 0:
    node, depth = q.popleft()
    if node == b:
        print(depth)
        break
    visited.add(node)
    candidates = [2*node, 10*node+1]
    for candidate in candidates:
        if candidate not in visited and candidate <= b:
            q.append((candidate, depth+1))


if node != b:
    print(-1)

