# 두 큐 합 같게 만들기
# 레벨 2
# 2022 KAKAO TECH INTERNSHIP


# 투 포인터
# 진짜로 큐 2개로 하면 시간초과
def solution(list1, list2):
    answer = -2

    queue = list1 + list2
    start = 0
    end = len(list1)

    total_sum = sum(list1) + sum(list2)
    list1_sum = sum(list1)
    if total_sum % 2 != 0:
        return -1

    max_round = len(queue) + 3

    for t in range(max_round):

        list2_sum = total_sum - list1_sum
        if list1_sum > list2_sum:
            list1_sum -= queue[start]
            start += 1
            start %= len(queue)
        elif list1_sum < list2_sum:
            list1_sum += queue[end]
            end += 1
            end %= len(queue)
        else:
            return t

    return -1
