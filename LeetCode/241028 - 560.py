# Subarray Sum Equals K
# Medium

class Solution:
    def subarraySum_wa(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0 for _ in range(n + 1)]
        # prefix_sum[i]: sum(nums[0:i])

        prefix_sum[1] = nums[0]
        for i in range(2, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        low = 0
        high = 1
        answer = 0
        while low < high < n + 1:
            value = prefix_sum[high] - prefix_sum[low]
            if value == k:
                answer += 1
                high += 1
            elif value < k:
                high += 1
            else:
                low += 1
                # 근데 음수가 있고 정렬되어 있지 않아서
                # 앞으로 간다고 커진다는 보장이 없음
                # two pointer 대신 nested iterate로 다 찾아야 할 듯

        return answer

    def subarraySum_tle(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0 for _ in range(n + 1)]
        # prefix_sum[i]: sum(nums[0:i])

        prefix_sum[1] = nums[0]
        for i in range(2, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        answer = 0
        # TLE
        for i in range(1, n + 1):
            for j in range(i):
                if prefix_sum[i] - prefix_sum[j] == k:
                    answer += 1

        return answer

    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        sums = {}
        sums[0] = 1
        curr = 0
        answer = 0

        # prefix sum의 기본 idea를 이용하되
        # prefix sum을 배열로 기록하는 대신 dict에 frequency를 기록
        # 이후, 매 step마다 현재의 prefix sum을 (k, current-k)로 쪼갬

        for i in range(n):
            curr += nums[i]

            if curr - k in sums:
                answer += sums[curr - k]

            if curr in sums:
                sums[curr] += 1
            else:
                sums[curr] = 1
        # print(sums)

        return answer

