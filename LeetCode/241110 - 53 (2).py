# Maximum Subarray
# Medium

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-math.inf for _ in range(n)]
        dp[0] = max(dp[0], nums[0])
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)
