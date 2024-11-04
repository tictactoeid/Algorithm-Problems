# Make Array Strictly Increasing
# Hard


from typing import *
import bisect
import math

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # arr2 = sorted(list(set(arr2)))


        # 1 5 3    [1, 2, 3, 4, 5]

        # bisect(1) = 0

        # bisect(3) = 2

        # -> 둘의 격차가 2이상이면 가운데 변경 ok
        # 1이하면 x 무조건 last 변경해야 함

        # 1 5 3 [0, 4, 5]
        # 1 1

        # dp[i] = (x, y), x는 operation count고 y는 last idx

        # 1 2 100 101 5 6 7 8 9 10 11

        # dp[i][x]: ith 원소까지 strictly increasing이고 x번 연산한 상태에서 last element, x <= i

        # -> 이미 subarray가 strictly increasing한다고 할지라도 subarray의 last element를 미리 줄여두는 것이 앞으로 이득이 될 수도 있음

        arr2 = sorted(list(set(arr2)))
        print(arr2)
        n = len(arr1)
        dp = [[math.inf for _ in range(n+1)] for _ in range(n)]


        dp[0][0] = arr1[0]
        if arr2[0] < arr1[0]:
            dp[0][1] = arr2[0]

        for i in range(1, n):
            for x in range(min(i+2, n+1)):  # i+1번의 연산 가능
                # TODO: current_min 부터 시작
                if dp[i-1][x] < arr1[i]:
                    # no additional operation
                    dp[i][x] = arr1[i]
                if x > 0:
                    idx = bisect.bisect_right(arr2, dp[i-1][x-1])
                    if idx < len(arr2):
                        dp[i][x] = min(dp[i][x], arr2[idx])

        print(dp)
        for x in range(n+1):
            if dp[-1][x] < math.inf:
                return x
        return -1


print(Solution().makeArrayIncreasing(
    [31,18,1,12,23,14,25,4,17,18,29,28,35,34,19,8,25,6,35],
    [13,10,25,18,3,8,37,20,23,12,9,36,17,22,29,6,1,12,37,6,3,14,37,2]
))