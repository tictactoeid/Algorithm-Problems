# Maximum Number of Events That Can Be Attended II
# Hard

class Solution:
    def maxValue_1(self, events: List[List[int]], k: int) -> int:
        # Approach 1
        # 현재 날짜 i에 대한 1차원 dp
        # k를 생각 안 해서 실패
        events.sort(key=lambda x: (x[1], x[2], x[0]))

        t = events[-1][1]  # end time of the last event
        n = len(events)
        print(events)

        dp = [0 for _ in range(t + 1)]
        dp[0] = 0
        # dp[i]: 현재 시각이 i일 때 얻을 수 있는 최대 value

        idx = 0
        for i in range(1, t + 1):
            dp[i] = dp[i - 1]
            while idx < n and events[idx][1] <= i:  # 현재 시각 이전에는 끝나는 event 고려
                event = events[idx]
                start, end, value = event
                dp[i] = max(dp[i], dp[max(start - 1, 0)] + value)
                idx += 1
        return dp[-1]

    def maxValue_2(self, events: List[List[int]], k: int) -> int:
        # Approach 2
        # k를 고려하여 2차원 dp로 확장
        # O(nt): t가 너무 커서 memory limit exceeded

        events.sort(key=lambda x: (x[1], x[2], x[0]))
        t = events[-1][1]  # end time of the last event
        n = len(events)

        dp = [[0 for _ in range(k + 1)] for _ in range(t + 1)]
        # dp[i][j]: 현재 시각 i, i 이내에 종료되는 event 중 j개를 고른 상황

        idx = 0
        for i in range(1, t + 1):
            for j in range(0, k + 1):
                dp[i][j] = dp[i - 1][j]

            while idx < n and events[idx][1] <= i:  # 현재 시각 이전에는 끝나는 event 고려
                event = events[idx]
                start, end, value = event
                for j in range(1, k + 1):
                    dp[i][j] = max(dp[i][j], dp[max(start - 1, 0)][j - 1] + value)
                idx += 1

        return max(dp[-1])

    # @lru_cache
    def dp(self, i, remain):
        if remain == 0 or i >= self.n:
            # self.answer = max(self.answer, total_value)
            return 0

        event = self.events[i]
        start, end, value = event

        # not pick
        not_pick = self.dp(i + 1, remain)

        # pick
        idx = bisect.bisect_left(self.events, [end + 1, 0, 0])
        pick = value + self.dp(idx, remain - 1)

        return max(not_pick, pick)

    def dp_memo(self, i, remain):
        if remain == 0 or i >= self.n:
            return 0
        if (i, remain) in self.memo:
            return self.memo[(i, remain)]

        event = self.events[i]
        start, end, value = event

        # not pick
        not_pick = self.dp_memo(i + 1, remain)

        # pick
        idx = bisect.bisect_left(self.events, [end + 1, 0, 0])
        pick = value + self.dp_memo(idx, remain - 1)

        self.memo[(i, remain)] = max(not_pick, pick)
        return self.memo[(i, remain)]

    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Approach 3: Knapsack, O(nk + nlogn)
        # state: (i, remain). i번째 event를 고를 차례이고 remain개의 event를 더 고를 수 있음
        # i번째를 고르지 않으면 단순히 (i+1, remain)
        # i번째를 고르면 다음에 고를 수 있는 event는 시작 시간이 end+1 이상인 event
        # 즉, event를 정렬해서 binary search로 다음 state (idx, remain-1)을 알아낸다

        events.sort()  # O(nlogn)
        self.events = events
        self.n = len(events)
        # return self.dp(0, k)

        self.memo = {}
        return self.dp_memo(0, k)  # O(nk)
