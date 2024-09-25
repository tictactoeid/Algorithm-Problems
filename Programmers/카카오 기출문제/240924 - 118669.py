# 등산 코스 정하기
# 레벨 3
# 2022 KAKAO TECH INTERNSHIP

# Dijkstra's ..?

# 다익스트라를 사용하되
# 길은 양방향이므로, 출발점 -> 산봉우리 만 고려
# 또한 거리는 그때까지의 거리 총합이 아닌, 지나온 edges의 weight 중 maximum

import math
import heapq


def solution(n, paths, gates, summits):
    edges = [[] for _ in range(n + 1)]
    for path in paths:
        i, j, w = path
        edges[i].append((j, w))
        edges[j].append((i, w))

    summits_set = set(summits)

    intensities = [math.inf for _ in range(n + 1)]
    q = []
    for gate in gates:
        intensities[gate] = 0
        heapq.heappush(q, (0, gate))

    while q:
        intensity, node = heapq.heappop(q)
        if node in summits_set:
            continue
        if intensities[node] < intensity:
            continue
        for edge in edges[node]:
            next, weight = edge

            next_intensity = max(intensity, weight)
            if next_intensity < intensities[next]:
                intensities[next] = next_intensity
                if next not in summits_set:
                    heapq.heappush(q, (next_intensity, next))

    gate_intensity = math.inf
    gate_summit = math.inf
    for summit in summits:
        if gate_intensity > intensities[summit]:
            gate_intensity = intensities[summit]
            gate_summit = summit
        elif gate_intensity == intensities[summit]:
            gate_summit = min(gate_summit, summit)

    return [gate_summit, gate_intensity]
