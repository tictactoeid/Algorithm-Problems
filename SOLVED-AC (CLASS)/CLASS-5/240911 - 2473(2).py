# 세 용액
# 골드 3

# 투 포인터: O(n^2)
# Python3 global 구현으로 시간 초과, sol() 따로 정의한 local 구현으로 통과

import math

n = int(input())
liquids = list(map(int, input().split()))


def sol(n, liquids):
    liquids.sort()

    result = [math.inf, None, None, None]

    for i in range(n - 2):  # O(n)
        j = i + 1
        k = n - 1
        l1 = liquids[i]
        while j != k:  # O(n-i)
            l2 = liquids[j]
            l3 = liquids[k]
            value = l1 + l2 + l3

            if abs(value) < abs(result[0]):
                result = [value, l1, l2, l3]

            if value > 0:
                # 더 작게
                k -= 1
            elif value < 0:
                j += 1
            else:
                # 종료
                print(l1, l2, l3)
                return

    print(result[1], result[2], result[3])

sol(n, liquids)
