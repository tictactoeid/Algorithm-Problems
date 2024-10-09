# Minimum Add to Make Parentheses Valid
# Medium

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0

        for x in s:
            if x == '(':
                stack.append(x)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1

        return count + len(stack)
