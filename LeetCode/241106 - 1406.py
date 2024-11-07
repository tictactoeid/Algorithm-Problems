# Stone Game III
# Hard

class Solution:
    def helper(self, i):
        if i >= self.n:
            return 0

        if i in self.memo:
            return self.memo[i]

        value = -math.inf
        for x in range(1, 4):
            if i + x > self.n:
                break
            # 얻을 수 있는 점수의 차: 1 <= x <= 3에 대하여
            # (앞에서부터 x개의 stone 점수의 합) - (i+x번 stone부터 상대가 최선을 다해 얻은 점수)
            value = max(value, sum(self.stoneValue[i:i + x]) - self.helper(i + x))

        self.memo[i] = value
        return value

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.n = len(stoneValue)
        self.stoneValue = stoneValue
        self.memo = {}
        self.helper(0)

        if self.memo[0] > 0:
            return "Alice"
        elif self.memo[0] == 0:
            return "Tie"
        else:
            return "Bob"

