# Maximum Sum Circular Subarray
# Medium


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        answer = dp[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            answer = max(dp[i], answer)

        # dp[0] = max(dp[-1] + nums[0], dp[0])
        # answer: maximum value of non-circular subarray

        # nums[-1], nums[0] 2가지를 무조건 포함하는 subarray 중 maximum을 찾아서 answer와 비교하면 됨
        # 그렇다면, nums[1:-1]에서 minimum subarray를 찾고 그걸 제외하면 됨

        if n >= 3:
            dp = [math.inf] * (n - 2)
            dp[0] = nums[1]
            tmp = dp[0]
            for i in range(1, n - 2):
                dp[i] = min(nums[i + 1], dp[i - 1] + nums[i + 1])
                tmp = min(dp[i], tmp)

            circular_maximum = sum(nums) - tmp
            answer = max(answer, circular_maximum)

        return answer

