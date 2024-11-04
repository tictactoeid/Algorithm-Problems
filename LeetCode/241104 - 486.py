# Predict the Winner
# Medium

class Solution:
    def score1(self, i, j, p1=True):
        if i > j:
            return 0

        if p1:
            left = self.nums[i] + self.score1(i + 1, j, False)
            right = self.nums[j] + self.score1(i, j - 1, False)
            return max(left, right)
        else:
            left = -self.nums[i] + self.score1(i + 1, j, True)
            right = -self.nums[j] + self.score1(i, j - 1, True)
            return min(left, right)

    def score2(self, i, j):
        if i > j:
            return 0
        elif i == j:
            return self.nums[i]

        left = self.nums[i] - self.score2(i + 1, j)  # 다음은 p2의 차례이므로, 뺀다.
        right = self.nums[j] - self.score2(i, j - 1)

        return max(left, right)

    def score3(self, i, j):
        # recursion with memoization
        if i > j:
            return 0
        elif i == j:
            return self.nums[i]
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        left = self.nums[i] - self.score3(i + 1, j)
        right = self.nums[j] - self.score3(i, j - 1)
        self.memo[(i, j)] = max(left, right)
        return self.memo[(i, j)]

    def predictTheWinner_recursion(self, nums: List[int]) -> bool:
        # O(2^n): score1(), score2()
        # O(n^2): score3(). recursion with memoization
        n = len(nums)
        self.nums = nums
        self.memo = {}
        # return self.score1(0, n-1, True) >= 0
        return self.score3(0, n - 1) >= 0

    def predictTheWinner(self, nums: List[int]) -> bool:
        # use dp array
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for diff in range(1, n):
            for i in range(0, n - diff):
                # compute dp[i][j]
                j = i + diff

                left = -dp[i + 1][j] if i + 1 <= j else 0
                left += nums[i]
                right = -dp[i][j - 1] if i <= j - 1 and j > 0 else 0
                right += nums[j]

                dp[i][j] = max(left, right)

        return dp[0][-1] >= 0
