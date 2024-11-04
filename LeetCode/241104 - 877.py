# Stone Game
# Medium

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def dp(self, i, j) -> int:
        piles = self.piles
        n = len(piles)
        if i > j:
            return 0

        if (n - (j - i)) % 2:
            # Alice plays
            left = self.dp(i + 1, j) + piles[i]  # if i > 0 else -math.inf
            right = self.dp(i, j - 1) + piles[j]  # if j < n else -math.inf
            return max(left, right)
        else:
            # Bob plays
            left = self.dp(i + 1, j) - piles[i]  # if i > 0 else math.inf
            right = self.dp(i, j - 1) - piles[j]  # if j < n else math.inf
            return min(left, right)

    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j]: piles[i] ~ piles[j] 남았을 때 Alice의 최대 점수
        self.piles = piles
        return bool(self.dp(0, len(piles) - 1) > 0)
