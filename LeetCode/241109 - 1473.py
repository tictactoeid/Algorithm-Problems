# Paint House III
# Hard

class Solution:
    def dp(self, idx, last_color, groups):
        # houses[idx] 칠할 차례
        # last_color = houses[idx - 1]
        # groups: 현재까지 group의 수

        if idx == self.m:
            if groups == self.target:
                return 0
            return math.inf

        if groups > self.target:
            return math.inf

        if (idx, last_color, groups) in self.memo:
            return self.memo[(idx, last_color, groups)]

        value = math.inf
        if self.houses[idx] != 0:
            if last_color == self.houses[idx]:
                value = self.dp(idx + 1, self.houses[idx], groups)
            else:
                value = self.dp(idx + 1, self.houses[idx], groups + 1)
        else:
            for i, cost in enumerate(self.cost[idx]):  # O(n) for each state
                color = i + 1
                if color == last_color:
                    value = min(value, self.dp(idx + 1, color, groups) + cost)
                else:
                    value = min(value, self.dp(idx + 1, color, groups + 1) + cost)

        self.memo[(idx, last_color, groups)] = value
        return value

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp
        # TC: O(m*n^2*target)
        # SC: O(m*n*target)

        # O(m*n*target) states, O(n) / state

        self.n = n
        self.houses = houses
        self.cost = cost
        self.m = m
        self.target = target

        self.memo = {}
        value = self.dp(0, math.inf, 0)
        if value == math.inf:
            return -1
        return value
    