# 표현 가능한 이진트리
# 레벨 3
# 2023 KAKAO BLIND RECRUITMENT

import math


def dfs(tree, target):
    root = len(tree) // 2

    if target == root:
        if tree[root] == "1":
            return True
        else:
            return False

    if tree[root] == "0":
        return False

    elif target < root:
        left_subtree = tree[:root]
        return dfs(left_subtree, target)

    else:
        right_subtree = tree[root+1:]
        return dfs(right_subtree, target-root-1)


def solution(numbers):
    answer = []
    for number in numbers:
        result = True
        tree = bin(number)[2:]  # 0b11..0
        n = math.ceil(math.log2(len(tree)+1))
        tree = "0" * (2**n - 1 - len(tree)) + tree

        for i in range(len(tree)):
            if tree[i] == "1":
                result = dfs(tree, i) and result
                if not result:
                    break

        if result:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([7, 42, 5, 63, 111, 95]))
