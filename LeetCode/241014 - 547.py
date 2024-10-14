# Number of Provinces
# Medium

# union-find: count the number of groups

class Solution:
    def union(self, i: int, j: int) -> None:
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i == parent_j:
            return

        self.parents[parent_j] = parent_i

    def find(self, i: int) -> int:
        if self.parents[i] == i:
            return i

        parent = self.parents[i]
        self.parents[i] = self.find(parent)
        return self.parents[i]

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.parents = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    self.union(i, j)

        answer = 0
        for i in range(n):
            parent = self.find(i)
            if i == parent:
                answer += 1

        return answer



