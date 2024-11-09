# Minimum Cost to Cut a Stick
# Hard

class Solution:
    def dp(self, i, j):
        if j - i <= 0 or i < 0 or j > self.n:
            return 0
        elif (i, j) in self.memo:
            return self.memo[(i, j)]
        else:
            idx1 = bisect.bisect_left(self.cuts, i + 1)

            value = math.inf
            for cut in self.cuts[idx1:]:
                if cut >= j:
                    break

                value = min(value, self.dp(i, cut) + self.dp(cut, j) + (j - i))

            if value == math.inf:
                value = 0

            self.memo[(i, j)] = value
            return value

    def minCost(self, n: int, cuts: List[int]) -> int:
        self.n = n
        self.cuts = sorted(cuts)
        self.memo = {}

        x = self.dp(0, n)
        return x
