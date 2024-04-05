# 숨바꼭질 (2)
# 골드 4

from collections import deque

n, k = map(int, input().split())

if n >= k:
    print(n-k)
    print(1)

else:
    # idea: bfs로 최단 거리를 탐색하되,
    # 최단 거리를 찾은 직후 바로 멈추지 않고
    # 같은 depth까지는 돌아보도록 함
    q = deque()
    visited = set()
    depth = 0
    visited.add(n)
    q.append((n, depth))
    fastest = -1
    cnt = 0

    while len(q) > 0:
        node, depth = q.popleft()
        if node == k:
            if fastest < 0:
                fastest = depth
                cnt += 1
                continue # 안 하면 시간 초과 발생
            elif fastest == depth:
                cnt += 1
                continue
            else:
                break

        visited.add(node)

        if node*2 <= k*2:
            candidates = [node-1, node+1, node*2]
        else:
            candidates = [node - 1, node + 1]

        for candidate in candidates:
            if candidate not in visited and candidate >= 0:
                # 음수쪽으로 계속 가면 시간 or 메모리 초과 발생
                q.append((candidate, depth + 1))

    print(fastest)
    print(cnt)
