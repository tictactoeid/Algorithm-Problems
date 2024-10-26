# Maximum Profit in Job Scheduling
# Hard

import bisect
from typing import *

# 답지 아예 안 보고 푼 몇 안 되는 문제..

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # dp
        # endTime 기준으로 정렬하고
        # dp[i]: i번째 (로 일찍 끝나는) job이 끝났을 시점에, 최대 profit

        # start_i 시점에 j번째 job까지 완료되었다면 => binary search로 찾음
        # dp[i] = max(dp[i-1], dp[j] + profit[i])

        n = len(startTime)
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        jobs.sort(key=lambda x: (x[1], -x[2]))

        # 주의
        # startTime, endTime, profit은 정렬된 배열이 아니므로 jobs를 통해서만 값에 접근해야 함

        dp = [0 for _ in range(n)]
        dp[0] = jobs[0][2]
        #print(jobs)

        for i in range(1, n):
            i_start = jobs[i][0]
            i_profit = jobs[i][2]
            j = bisect.bisect_right(jobs, i_start, key=lambda x: x[1])
            if j > 0:
                dp[i] = max(dp[i-1], dp[j-1] + i_profit)
            else:
                dp[i] = max(dp[i-1], i_profit)
        #print(dp)
        return dp[-1]


