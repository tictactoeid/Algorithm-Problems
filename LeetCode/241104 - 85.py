# Maximal Rectangle
# Hard

# 84. Largest Rectangle in Histogram의 풀이를 90도 돌려서 응용
# 생각해보니 굳이 돌릴 필요 없었을듯?

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # TC: O(mn)
        # SC: O(mn)이나 O(m+n)까지 최적화 가능할 듯
        # dp배열은 사실 필요없고, lengths 배열은 현재 column만 가지고 있으면 됨

        m, n = len(matrix), len(matrix[0])
        lengths = [[0 for _ in range(n)] for _ in range(m)]
        # 현재 row만 봤을 때, lengths[i]는 row[i]부터 시작하여 연속한 1의 갯수

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    lengths[i][j] = lengths[i][j - 1] + 1 if j > 0 else 1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        answer = 0
        for j in range(n):
            # (left_width + 1 + right_width) * length[i][j]

            # 나보다 위에 있는 lengths 원소 중 나보다 작은 첫 번째 원소
            stack = []
            for i in range(m):
                while stack and stack[-1][0] >= lengths[i][j]:
                    stack.pop()
                if stack:
                    idx = stack[-1][1]
                else:
                    idx = -1
                stack.append((lengths[i][j], i))

                left_width = i - idx - 1
                if lengths[i][j] != 0:
                    dp[i][j] = left_width

            # 나보다 오른쪽에 있는 원소 중 나보다 작은 첫 번째 원소
            stack = []
            for i in range(m - 1, -1, -1):
                while stack and stack[-1][0] >= lengths[i][j]:
                    stack.pop()
                if stack:
                    idx = stack[-1][1]
                else:
                    idx = m
                stack.append((lengths[i][j], i))

                right_width = idx - i - 1
                if lengths[i][j] != 0:
                    dp[i][j] += right_width + 1
                    dp[i][j] *= lengths[i][j]
                    answer = max(answer, dp[i][j])

        return answer
