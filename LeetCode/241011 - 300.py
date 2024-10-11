# Longest Increasing Subsequence
# Medium

import bisect

class Solution:
    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        # O(n^2)
        n = len(nums)
        dp = [1 for _ in range(n)]
        # dp[i]: nums[0:i+1]의 LIS 길이

        dp[0] = 1
        for i in range(1, n):
            for k in range(i):
                if nums[k] < nums[i]:
                    dp[i] = max(dp[i], dp[k] + 1)

        print(dp)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(nlogn)

        # 빈 배열에서 시작
        # nums의 각 원소를 이분탐색
        # 만약 answer의 마지막 원소보다 크다면 answer 길이를 늘림

        # answer의 마지막 원소보다 작다면 index를 찾아 해당 원소를 대체
        # 예를 들어 answer = [2], 현재 num = 1이라면
        # answer = [1]로 대체하는 것이 이후 유리
        answer = []
        n = len(nums)
        for i in range(n):
            idx = bisect.bisect_left(answer, nums[i])
            if idx >= len(answer):
                answer.append(nums[i])
            else:
                answer[idx] = nums[i]

        return len(answer)

