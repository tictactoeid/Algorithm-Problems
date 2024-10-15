# Combination Sum IV
# Medium

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = [num for num in nums if num <= target]
        nums.sort()

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i - num]

        return dp[target]
