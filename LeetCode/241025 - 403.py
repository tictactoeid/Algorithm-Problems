# Frog Jump
# Hard

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False

        dp = {i: set() for i in stones}
        dp[stones[1]].add(1)
        n = len(stones)

        # 모든 stone에서 현재 stone으로 올 수 있다고 하면, dp[current]의 최대 길이는 n
        # 즉, O(n)

        # print(dp)

        for i in range(1, n):
            stone = stones[i]
            for unit in dp[stone]:
                for jump in range(max(1, unit - 1), unit + 2):
                    next_stone = stone + jump
                    if next_stone in dp:
                        dp[next_stone].add(jump)
        # print(dp)
        return bool(dp[stones[-1]])


