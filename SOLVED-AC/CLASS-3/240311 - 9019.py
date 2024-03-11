# DSLR
# 골드 4

# Pypy3으로 제출 시 시간 초과 없이 통과

from collections import deque

reg = 0


def DSLR(n):
    return [('D', 2*n % 10000),
            ('S', (n-1) % 10000),
            ('L', (n%1000) * 10 + n // 1000),
            ('R', (n%10) * 1000 + n // 10)]


t = int(input())

for _ in range(t):
    init, result = map(int, input().split())
    q = deque([init])
    visited = {init: (-1, '')}
    # { 1234: (2341, L) }
    # { child: (parent, command) }
    node = init
    while len(q) > 0:
        node = q.popleft()
        if node == result:
            break

        for child in DSLR(node):
            if child[1] not in visited.keys():
                visited[child[1]] = (node, child[0])
                q.append(child[1])

    output = ''

    while node >= 0:
        command = visited[node][1]
        node = visited[node][0]
        output = command + output
    print(output)







