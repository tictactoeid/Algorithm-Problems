# 체육복
# 레벨 1
# 그리디


def solution(n, lost, reserve):
    answer = 0
    borrow = []
    count = 0

    lost.sort()
    reserve.sort()

    for student in lost:
        if student in reserve:
            reserve.remove(student)
            continue
        if student - 1 in reserve and student - 1 not in lost:
            reserve.remove(student - 1)
            continue
        if student + 1 in reserve and student + 1 not in lost:
            reserve.remove(student + 1)
            continue
        count += 1

    answer = n - count

    return answer
