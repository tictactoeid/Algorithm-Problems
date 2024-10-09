# Longest Valid Parentheses
# Hard

from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        valid = [False for _ in range(len(s))]
        result = 0

        for i, x in enumerate(s):
            if x == '(':
                stack.append(('(', i))
            else:
                count = 1
                start_idx = i
                while count:
                    if not stack:  # invalid
                        break
                    char, idx = stack.pop()
                    start_idx = min(start_idx, idx)
                    if char == ')':
                        count += 1
                    else:
                        count -= 1
                if count == 0:
                    for j in range(start_idx, i + 1):
                        valid[j] = True

        q = deque(valid)
        count = 0
        while q:
            x = q.popleft()
            if x:
                count += 1
            else:
                result = max(result, count)
                count = 0
        result = max(result, count)
        return result
