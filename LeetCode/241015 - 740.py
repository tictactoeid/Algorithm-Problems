# Delete and Earn
# Medium

from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)

        nums_set = set(nums)
        nums = sorted(list(nums_set))
        n = len(nums)

        dp = [0 for _ in range(n + 1)]
        dp[0] = 0

        dp[1] = count[nums[0]] * nums[0]


        for i in range(2, n + 1):
            # 아래 알고리즘을 max() 없이 O(n) 으로 가능하도록 발전시킴
            if nums[i - 1] - 1 == nums[i - 2]:
                dp[i] = max(count[nums[i - 1]] * nums[i - 1] + dp[i - 2], dp[i - 1])
            else:
                dp[i] = count[nums[i - 1]] * nums[i - 1] + dp[i - 1]
            # dp[i]: nums[i-1]을 고르는 경우의 최댓값
            # idx = i-1
            # dp[i] = count[nums[idx]] * nums[idx]
            # dp[i] += max(dp[:i]) if nums[idx] - 1 != nums[idx-1] else max(dp[:i-1])

        #print(dp)
        return dp[-1]
