# Stone Game II
# Medium

class Solution:
    def helper(self, i, m):
        if i >= self.n:
            return 0
        if i + 2 * m >= self.n:
            self.memo[(i, m)] = sum(self.piles[i:])
            return self.memo[(i, m)]
        if (i, m) in self.memo:
            return self.memo[(i, m)]

        value = 0
        for x in range(1, 2 * m + 1):
            if i + x > self.n:
                break
            # 현재 상태에서 Alice가 얻을 수 있는 최댓값은
            # 남은 모든 pile 중 (self.piles[i:])
            # Bob이 얻을 수 있는 최대 점수 (self.helper(i+x, max(m, x)))
            # 를 제외
            value = max(value, (sum(self.piles[i:]) - self.helper(i + x, max(m, x))))
            # use suffix sum to optimize

        self.memo[(i, m)] = value
        return value

    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles
        self.n = len(piles)
        self.memo = {}
        self.helper(0, 1)
        # print(self.memo)

        return self.memo[(0, 1)]

