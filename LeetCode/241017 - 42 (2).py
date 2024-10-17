# Trapping Rain Water
# Hard

# 모든 칸에 대하여, 아래 2가지 정보가 필요
# 나보다 왼쪽에 있는 벽 중 가장 높은 것
# 나보다 오른쪽에 있는 벽 중 가장 높은 것

# (두 벽 중 낮은 쪽의 높이) - (현재 칸의 높이)가 현재 칸에 최대로 들어갈 수 있는 물의 양
# 기존에는 dp로 풀이

# monotonic stack에서, stack에 append할 때
# stack[-1] 값이 나보다 큰 직전의 값이라면
# stack[0]은 이전 값들 중 가장 큰 값이므로 이를 이용해서 해결


class Solution:
    def monotonic(self, stack: List[int], array: List[int], i: int):
        while stack and stack[-1][0] <= self.height[i]:
            stack.pop()

        if stack:
            array[i] = stack[0][1]  # stack[-1][1]

        stack.append((self.height[i], i))
        return stack, array

    def trap(self, height: List[int]) -> int:
        n = len(height)
        self.height = height

        stack = []  # (value, idx)
        array_left = [-1 for _ in range(n)]
        for i in range(n):
            stack, array_left = self.monotonic(stack, array_left, i)

        stack = []  # (value, idx)
        array_right = [-1 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            stack, array_right = self.monotonic(stack, array_right, i)

        answer = 0
        for i in range(n):
            left_wall = height[array_left[i]] if array_left[i] >= 0 else 0
            right_wall = height[array_right[i]] if array_right[i] >= 0 else 0
            answer += max(0, min(left_wall, right_wall) - height[i])

        return answer
