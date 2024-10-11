# Container With Most Water
# Medium

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        answer = 0
        start = 0
        end = n - 1

        while start <= end:
            answer = max(answer, (end - start) * min(height[start], height[end]))

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return answer
