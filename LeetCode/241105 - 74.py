# Search a 2D Matrix
# Medium

class Solution:
    def convert(self, idx):
        return (idx // self.n, idx % self.n)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        self.n = n

        low = 0
        high = m*n - 1

        while low <= high:
            mid = (low + high) // 2
            x, y = self.convert(mid)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
