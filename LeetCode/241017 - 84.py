# Largest Rectangle in Histogram
# Hard

# Monotonic stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 배열의 각 원소에 대하여, 2가지 정보가 필요
        # 나보다 왼쪽의 원소들 중, 나와 가장 가까이 있으면서 나보다 작은 첫 번째 수
        # 나보다 오른쪽의 원소들 중 또한 마찬가지

        # brute force로 O(n^2)로 풀 수 있지만
        # monotonic stack을 적용하면 이를 O(n)으로 풀 수 있다.

        n = len(heights)
        stack_left = []  # (value, idx)
        stack_right = []
        first_small_left_idx = [-1 for _ in range(n)]
        first_small_right_idx = [n for _ in range(n)]

        for idx, value in enumerate(heights):
            while stack_left and stack_left[-1][0] >= value:
                stack_left.pop()
            # 자신 이상의 원소를 모두 제거했으므로 stack은 monotonic increasing
            if stack_left:
                first_small_left_idx[idx] = stack_left[-1][1]
            stack_left.append((value, idx))

            # 오른쪽도 작은 원소를 골라야 하므로 monotonic increasing, 단 역순으로 iterate

        for idx in range(n - 1, -1, -1):
            value = heights[idx]
            while stack_right and stack_right[-1][0] >= value:
                stack_right.pop()

            if stack_right:
                first_small_right_idx[idx] = stack_right[-1][1]
            stack_right.append((value, idx))

        # print(first_small_left_idx)
        # print(first_small_right_idx)

        answer = 0

        for idx in range(n):
            value = (first_small_right_idx[idx] - first_small_left_idx[idx] - 1) * heights[idx]
            answer = max(answer, value)

        return answer
