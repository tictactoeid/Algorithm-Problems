# 숨바꼭질 3
# 골드 5


from collections import deque

n, k = map(int, input().split())

if n >= k:
    print(n-k)

else:
    q = deque()
    visited = set()
    depth = 0
    node = n

    visited.add(node)
    q.append((node, depth))

    while len(q) > 0:
        #print(q)
        node, depth = q.popleft()
        if node == k:
            print(depth)
            break

        visited.add(node)
        if node-1 >= 0:
            adjs = [(node-1, 1), (node+1, 1)] # 1초 소요
        else:
            adjs = [(node+1, 1)]

        #if node * 2 <= k * 2:
        #    adjs.append((node * 2, 0))
        i = node * 2
        while k*2 >= i > 0:
            adjs.append((i, 0))
            if i-1 >= 0:
                adjs.append((i-1, 1)) # 1초 소요
            adjs.append((i+1, 1))
            i *= 2


        for adj in adjs:
            if adj[0] not in visited: # adj[0]
                # visited.add(adj[0])
                # 여기서 먼저 찾은 경로가 최적이 아닐 수 있기 때문에
                # visited로 표시하면 안 됨
                # queue에서 뺄 때는 그게 최적이라는 보장이 있음. 그때 visited로 표시ㅐ
                if adj[1] == 1:
                    q.append((adj[0], depth + 1))
                else:
                    q.appendleft((adj[0], depth))


