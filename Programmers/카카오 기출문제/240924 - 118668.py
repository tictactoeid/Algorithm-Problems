# 코딩 테스트 공부
# 레벨 3
# 2022 KAKAO TECH INTERNSHIP

# Dijkstra's algorithm

import heapq
import math



MAX = 150  # for debug


def solution(alp, cop, problems):
    answer = math.inf

    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    # 알고력과 코딩력을 1 늘리는 것은 사실상 시간 1짜리 문제를 푸는 것과 같다

    target_alp = max(row[0] for row in problems)
    target_cop = max(row[1] for row in problems)

    distance = [[math.inf for _ in range(MAX+1)] for _ in range(MAX+1)]

    for i in range(alp+1):
        for j in range(cop+1):
            distance[i][j] = 0


    q = []

    heapq.heappush(q, (0, alp, cop))
    while q:
        curr_dist, curr_alp, curr_cop = heapq.heappop(q)
        if distance[curr_alp][curr_cop] < curr_dist:
            continue

        for problem in problems:
            if curr_alp < problem[0] or curr_cop < problem[1]:
                continue

            next_alp = min(curr_alp + problem[2], MAX)
            next_cop = min(curr_cop + problem[3], MAX)
            next_dist = curr_dist + problem[4]

            if next_dist < distance[next_alp][next_cop]:
                distance[next_alp][next_cop] = next_dist
                heapq.heappush(q, (next_dist, next_alp, next_cop))

    for i in range(target_alp, MAX+1):
        for j in range(target_cop, MAX+1):
            answer = min(answer, distance[i][j])

    return answer

