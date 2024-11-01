# Number of Connected Components in an Undirected Graph
# Medium

class Solution:
    def find(self, node: int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, x: int, y: int) -> None:
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 == p2:
            return
        self.parents[p1] = p2

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parents = [i for i in range(n)]
        for x, y in edges:
            self.union(x, y)

        count = 0
        for i in range(n):
            if i == self.find(i):
                count += 1

        return count
