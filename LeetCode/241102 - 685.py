# Redundant Connection II
# Hard

class Solution:
    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)

        if p1 != p2:
            self.parents[p2] = p1

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # 주어진 그래프: tree + 1 additional edge
        # indegree가 2인 node가 있는 경우
        # 없는 경우 cycle

        n = len(edges)
        self.parents = [i for i in range(n + 1)]
        indegrees = {x: [] for x in range(1, n + 1)}
        candidate = None

        for x, y in edges:
            if candidate is None:
                indegrees[y].append(x)
                if len(indegrees[y]) == 2:
                    candidate = y

        if candidate is None:  # detect cycle
            for x, y in edges:
                if self.find(x) == self.find(y):
                    return [x, y]
                self.union(x, y)
        else:  # use candidate
            x1, x2 = indegrees[candidate]
            # [x1, candidate], [x2, candidate] 둘 중 하나가 정답
            # input에서 나중에 등장한 [x2, candidate]를 제거했을 때 정상적인 tree가 만들어지는지 확인

            for x, y in edges:
                if x == x2 and y == candidate:
                    continue
                self.union(x, y)

            root = None
            for x in range(1, n + 1):
                if root is None:
                    root = self.find(x)
                else:
                    if root != self.find(x):
                        # invalid tree이므로 [x2, candidate]를 제거할 수 없음
                        return [x1, candidate]

            return [x2, candidate]

