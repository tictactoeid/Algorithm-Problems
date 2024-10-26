# House Robber II
# Medium

class Solution:
    def rob_linear_space(self, nums: List[int]) -> int:
        # basic dp
        # O(n) space, O(n) time

        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [0, nums[0]]
        # 첫 번째 집을 훔치지 않은 경우, 훔친 경우

        for i in range(1, n):
            if i > 1:
                dp[i][0] = max(dp[i - 1][0], dp[i - 2][0] + nums[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][1] + nums[i]) if i < n - 1 else dp[i - 1][1]
            else:
                dp[i][0] = max(dp[i - 1][0], nums[i])
                dp[i][1] = max(dp[i - 1][1], nums[i]) if i < n - 1 else dp[i - 1][1]

        return max(dp[-1])

    # 첫 번째 집을 훔치지 않은 경우, nums[1:]에 대해 생각하면 됨
    # 훔친 경우, 마지막 집을 훔칠 수 없으므로 nums[:-1]에 대해 생각하면 됨
    # 또한 직전 2개의 값만 참조하므로 dp 배열 전체가 아닌 2개의 변수만 사용하여 O(1) space로 해결할 수 있음

    def rob(self, nums):
        # O(1) space, O(n) time
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums):
        prev = 0
        curr = 0
        for num in nums:
            tmp = max(curr, prev + num)
            prev = curr
            curr = tmp

        return curr
