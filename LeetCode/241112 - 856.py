# Score of Parentheses
# Medium
# Moloco 기출

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        l_cnt = 0  # handle invalid input, follow-up question in the interview
        r_cnt = 0

        for x in s:
            if x == "(":
                stack.append(0)
                l_cnt += 1
            elif x == ")":
                r_cnt += 1
                if r_cnt > l_cnt:
                    return 0
                curr_score = 0
                while stack and stack[-1] != 0:
                    curr_score += stack.pop()
                if stack and stack[-1] == 0:
                    stack.pop()
                stack.append(max(curr_score * 2, 1))
            else:
                continue

        if not stack or l_cnt != r_cnt:
            return 0
        return sum(stack)
