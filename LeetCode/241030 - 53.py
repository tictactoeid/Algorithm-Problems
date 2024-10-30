# Maximum Subarray
# Medium

class Solution:
    def maxSubArray_linear(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)

    def findMax(self, nums, start, end):
        if start == end:
            return nums[start]
        elif start > end:
            return -math.inf

        mid = (start + end) // 2
        left_max = self.findMax(nums, start, mid - 1)
        right_max = self.findMax(nums, mid + 1, end)

        cross_max = -math.inf

        right_prefix_max = 0
        tmp = 0
        for i in range(mid + 1, end + 1):
            tmp += nums[i]
            right_prefix_max = max(right_prefix_max, tmp)

        left_prefix_max = 0
        tmp = 0
        for i in range(mid - 1, start - 1, -1):
            tmp += nums[i]
            left_prefix_max = max(left_prefix_max, tmp)

        cross_max = left_prefix_max + nums[mid] + right_prefix_max

        return max(left_max, right_max, cross_max)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.findMax(nums, 0, len(nums) - 1)
    