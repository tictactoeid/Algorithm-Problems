# Jump Game II
# Medium

import math


class Solution:
    def jump_nsquare(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [math.inf for _ in range(n)]

        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0 for _ in range(n)]

        count = 0
        maximum = 0
        end = 0
        for i in range(n - 1):
            maximum = max(maximum, nums[i] + i)

            if maximum >= n - 1:
                return count + 1

            if i == end:
                count += 1
                end = maximum

        return count
