# Maximum Score from Performing Multiplication Operations
# Hard


class Solution:
    # Greedy인줄 알았다, 문제를 잘 읽자!

    def helper(self, low, high):
        i = (low - 0) + (self.n - 1 - high)

        if i >= self.m or high < low:
            return 0

        if (low, high) in self.memo:
            return self.memo[(low, high)]

        left = self.nums[low] * self.multipliers[i] + self.helper(low + 1, high)
        right = self.nums[high] * self.multipliers[i] + self.helper(low, high - 1)
        self.memo[(low, high)] = max(left, right)

        return self.memo[(low, high)]

    def maximumScore_1(self, nums: List[int], multipliers: List[int]) -> int:
        # O(n^2)
        # state: low, high, i
        # low, high는 nums에서 남은 배열
        # i는 ith operation을 의미
        # 그런데 low와 high가 있으면 i를 구할 수 있으므로 2d dp로 가능

        self.n = len(nums)
        self.m = len(multipliers)
        self.memo = {}
        self.nums = nums
        self.multipliers = multipliers
        return self.helper(0, self.n - 1)

    def helper_2(self, low, i):
        high = low - i + self.n - 1

        if high < low or i >= self.m:
            return 0
        if (low, i) in self.memo:
            return self.memo[(low, i)]

        left = self.nums[low] * self.multipliers[i] + self.helper_2(low + 1, i + 1)
        right = self.nums[high] * self.multipliers[i] + self.helper_2(low, i + 1)
        self.memo[(low, i)] = max(left, right)

        return self.memo[(low, i)]

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # O(m^2)
        # 반대로 low와 i를 가지고 high를 구하면 state 수가 O(m^2)으로 줄어듦

        self.n = len(nums)
        self.m = len(multipliers)
        self.memo = {}
        self.nums = nums
        self.multipliers = multipliers
        return self.helper_2(0, 0)
