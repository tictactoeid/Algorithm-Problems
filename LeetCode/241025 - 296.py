# Best Meeting Point
# Hard

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        vertical = []
        horizontal = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    vertical.append(i)
                    horizontal.append(j)
        vertical.sort()
        horizontal.sort()
        # if len(vertical) % 2 == 1:
        vertical_median = vertical[len(vertical) // 2]
        horizontal_median = horizontal[len(horizontal) // 2]
        ans = 0
        for ver in vertical:
            ans += abs(ver - vertical_median)
        for hor in horizontal:
            ans += abs(hor - horizontal_median)
        # print(vertical, vertical_median)
        # print(horizontal, horizontal_median)
        return ans
