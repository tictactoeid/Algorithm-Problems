# Maximum Product Subarray
# Medium

import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[-math.inf, math.inf] for _ in range(len(nums))]
        # consider minus sign

        dp[0][0] = nums[0]
        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])
            dp[i][1] = min(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])

        #print(dp)
        return max(map(max, dp))
