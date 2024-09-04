# 타겟 넘버
# 레벨 2
# DFS / BFS

from itertools import product


def solution(numbers, target):
    answer = 0
    operators = ['+', '-']
    comb = product(operators, repeat=len(numbers))
    for i in comb:
        oper_sets = zip(i, numbers)
        result = 0
        for oper_set in oper_sets:
            if oper_set[0] == '+':
                result += oper_set[1]
            else:
                result -= oper_set[1]
        if result == target:
            answer += 1

    return answer
