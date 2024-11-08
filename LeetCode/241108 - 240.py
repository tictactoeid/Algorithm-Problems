# Search a 2D Matrix II
# Medium

class Solution:
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        # Approach 1: Binary Search
        # O(mlogn)
        # binary search를 대각선으로 쓰는 풀이가 있긴 한데 그냥 각 row에 대해 binary search해도 복잡도가 O(nlogn)임..

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            idx = bisect.bisect_left(matrix[i], target)
            if idx < n and matrix[i][idx] == target:
                return True

        return False

    def searchMatrix(self, matrix, target):
        # Approach 2: reduce search space
        # TC: O(m+n), SC: O(1)
        m, n = len(matrix), len(matrix[0])

        i, j = 0, n - 1

        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == target:
                return True

            left = matrix[i][j - 1] if j > 0 else -math.inf
            down = matrix[i + 1][j] if i < m - 1 else +math.inf

            if target <= left:
                i, j = i, j - 1
            elif target >= down:
                i, j = i + 1, j
            elif left <= target <= down:
                i, j = i + 1, j - 1

        return False


