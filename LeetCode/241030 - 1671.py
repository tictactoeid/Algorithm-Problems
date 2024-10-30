# Minimum Number of Removals to Make Mountain Array
# Hard


class Solution:
    def minimumMountainRemovals_nsquare(self, nums: List[int]) -> int:
        # O(n^2)

        # mountain의 꼭대기 index가 x이면
        # nums[:x+1]에서는 LIS를
        # nums[x:] 에서는 (reversed) LIS를 고르면 된다
        # LIS는 1차원 dp

        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        # dp[i][0]: nums[:i+1]의 LIS 길이
        # dp[i][1]: nums[i:] 의 reversed LIS 길이

        # retval: min(n - sum(dp[i]) + 1), 단 무조건 증가 감소 구간이 모두 있어야 하므로 둘 중 하나라도 1이면 제외

        # O(n^2), bisect를 이용하면 더 빠르게 가능
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][0] + 1)

        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][1] + 1)

        # print(dp)

        answer = math.inf

        for i in range(n):
            if 1 in dp[i]:
                continue
            value = n - sum(dp[i]) + 1
            answer = min(answer, value)

        return answer  # min([n-sum(dp[i])+1 for i in range(n)])

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # O(nlogn)
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]  # dp 아니긴 한데 위 코드랑 통일을 위해 편의상..

        tmp = []
        for i in range(n):
            idx = bisect.bisect_left(tmp, nums[i])
            if idx >= len(tmp):
                tmp.append(nums[i])
            else:
                tmp[idx] = nums[i]
            dp[i][0] = len(tmp)

        tmp = []
        for i in range(n - 1, -1, -1):
            idx = bisect.bisect_left(tmp, nums[i])
            if idx >= len(tmp):
                tmp.append(nums[i])
            else:
                tmp[idx] = nums[i]
            dp[i][1] = len(tmp)

        answer = math.inf

        for i in range(n):
            if 1 in dp[i]:
                continue
            value = n - sum(dp[i]) + 1
            answer = min(answer, value)

        return answer  # min([n-sum(dp[i])+1 for i in range(n)])
