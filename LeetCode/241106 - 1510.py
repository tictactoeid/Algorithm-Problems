# Stone Game IV
# Hard

class Solution:
    def helper(self, i):
        # return True if can win
        # return False otherwise
        if i <= 0:
            return False

        if i in self.memo:
            return self.memo[i]

        for x in range(1, int(sqrt(i)) + 1):
            result = self.helper(i - x ** 2)
            if not result:
                # Bob loses, so Alice wins. return True.
                self.memo[i] = True
                return True
        self.memo[i] = False
        return False

    def winnerSquareGame(self, n: int) -> bool:
        self.memo = {}
        return self.helper(n)
