# Remove Invalid Parentheses
# Hard

class Solution:
    # left_remove = 0
    # right_remove = 0
    remove = 0
    answer = []

    def __init__(self):
        self.remove = 0
        self.answer = []

    def count(self, s: str) -> None:
        stack = []
        cnt = 0
        for x in s:
            if x == '(':
                stack.append(x)
            elif x == ')':
                if stack:
                    stack.pop()
                else:
                    cnt += 1
        # self.left_remove = len(stack)
        # self.right_remove = cnt
        self.remove = len(stack) + cnt

    def validate(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(':
                stack.append(x)
            elif x == ')':
                if not stack:
                    return False
                stack.pop()
        if stack:
            return False
        return True

    def backtracking(self, s: str, start_idx: int, count: int):
        if count == self.remove:
            if self.validate(s):
                if s not in self.answer:
                    self.answer.append(s)
                return

        for i in range(start_idx, len(s)):
            if s[i] == '(' or s[i] == ')':
                self.backtracking(s[:i] + s[i + 1:], i, count + 1)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.count(s)
        self.backtracking(s, 0, 0)
        return self.answer
