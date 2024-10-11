# Trapping Rain Water
# Hard

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left_height = [0 for _ in range(n)]  # dp
        max_right_height = [0 for _ in range(n)]  # dp

        for i in range(1, n):
            max_left_height[i] = max(max_left_height[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            max_right_height[i] = max(max_right_height[i + 1], height[i + 1])

        answer = 0
        for i in range(n):
            answer += max(min(max_left_height[i], max_right_height[i]) - height[i], 0)

        return answer
