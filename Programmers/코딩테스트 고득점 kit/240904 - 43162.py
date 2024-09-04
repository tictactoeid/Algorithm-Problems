# 네트워크
# 레벨 3
# DFS / BFS

from collections import deque


def bfs(i, network_number, computers, network_info):
    q = deque()
    q.append(i)

    while q:
        node = q.popleft()
        network_info[node] = network_number
        for next in range(len(computers)):
            if not network_info[next] and computers[node][next]:
                q.append(next)
                network_info[node] = network_number
    return network_info


def solution(n, computers):
    # answer = 0
    network_info = [0 for _ in range(len(computers))]  # visited + 번호 매기는 역할
    network_number = 1
    for i in range(len(computers)):
        if not network_info[i]:
            network_info = bfs(i, network_number, computers, network_info)
            network_number += 1

    return network_number - 1


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
