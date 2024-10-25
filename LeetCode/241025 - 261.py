# Graph Valid Tree
# Medium

class Solution:
    def find(self, i):
        if self.parents[i] == i:
            return i
        p = self.parents[i]
        self.parents[i] = self.find(p)
        return self.parents[i]

    def union(self, i, j):
        p1 = self.find(i)
        p2 = self.find(j)
        if p1 == p2:
            return
        self.parents[p2] = p1

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.parents = [i for i in range(n)]

        for edge in edges:
            x, y = edge
            p1, p2 = self.find(x), self.find(y)
            if p1 == p2:
                return False
            self.union(x, y)

        root = None
        for i in range(n):
            if root != self.find(i) and root is not None:
                return False
            root = self.find(i)

        return True