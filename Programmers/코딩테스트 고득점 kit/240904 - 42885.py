# 구명보트
# 레벨 2
# 그리디

from collections import deque


def solution_timeout(people, limit):  # O(n^2)
    answer = 0

    people.sort(reverse=True)
    exited = [False for _ in range(len(people))]

    for i in range(len(people)):
        if exited[i]:
            continue
        maximum_idx = -1

        for j in range(len(people)-1, i, -1):
            if exited[j]:
                continue
            if people[i] + people[j] <= limit:
                maximum_idx = j
            else:
                break
        if maximum_idx != -1:
            exited[maximum_idx] = True

        exited[i] = True
        answer += 1

    return answer


def solution(people, limit):  # 정렬에 O(nlogn)
    answer = 0
    people = deque(sorted(people, reverse=True))

    # 2명이 탈 수 있는지 없는지가 중요
    # "누가" 탔는지는 중요치 않음
    # (안 탄) 가장 무거운 사람 + 가장 가벼운 사람 -> 나갈 수 있다면
    # 그냥 그렇게 2명 내보내면 됨, 굳이 최적으로 2명을 내보낼 필요가 없음
    # 어차피 무거운 사람부터 내보낼 것이기 때문에, 가벼운 사람이 탈 수 있는 여유 무게도 계속 늘어나기 때문

    while people:
        if people[0] + people[-1] > limit:
            people.popleft()
        else:
            people.popleft()
            if people:  # 예외 처리
                people.pop()
        answer += 1

    return answer
