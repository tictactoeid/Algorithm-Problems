# Optimal Account Balancing
# Hard

# 처음에 Greedy로 접근했으나 사실 Greedy가 아니라는 것을 알아내기는 함
# Backtracking이라는 것을 알아내는 것과, 이를 디테일하게 구현하는 것이 어려웠음

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # balance = [0 for _ in range(n)]
        n = 0
        for tr in transactions:
            n = max(n, tr[0], tr[1])
        n += 1
        balance = [0 for _ in range(n)]

        for x, y, amount in transactions:
            balance[x] -= amount
            balance[y] += amount

        balance = [x for x in balance if x != 0]
        balance.sort(key=lambda x: abs(x))

        self.count = math.inf
        self.dfs(balance, 0, 0)
        return self.count

        # it is not greedy!

    def dfs(self, balance, idx, count):
        # print(balance, idx, count)
        if idx >= len(balance):
            self.count = min(count, self.count)
            return

        if balance[idx] == 0:
            return self.dfs(balance, idx + 1, count)

        for i in range(idx + 1, len(balance)):
            if balance[i] == 0:
                continue
            elif balance[i] * balance[idx] > 0:
                continue

            else:
                if abs(balance[idx]) <= abs(balance[i]):
                    tmp = [balance[idx], balance[i]]
                    balance[idx], balance[i] = 0, sum(tmp)
                    self.dfs(balance, idx + 1, count + 1)
                    balance[idx], balance[i] = tmp[0], tmp[1]
                else:
                    tmp = [balance[i], balance[idx]]
                    balance[i], balance[idx] = 0, sum(tmp)
                    self.dfs(balance, idx, count + 1)
                    balance[i], balance[idx] = tmp[0], tmp[1]
