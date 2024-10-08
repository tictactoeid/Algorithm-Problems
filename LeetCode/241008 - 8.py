# String to Integer (atoi)
# Medium

class Solution:
    def isDigit(self, s: str) -> bool:
        if len(s) > 1:
            return None
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        return s in digits

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        answer = []
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            sign = +1
            start = 1
        else:
            sign = +1
            start = 0

        s = s[start:]
        s = s.lstrip('0')

        for i in range(len(s)):
            if self.isDigit(s[i]):
                answer.append(s[i])
            else:
                break
        print(answer)
        result = "".join(answer)
        if result:
            result = int(result) * sign
            if result > 2 ** 31 - 1:
                result = 2 ** 31 - 1
            elif result < -2 ** 31:
                result = -2 ** 31
            return result
        else:
            return 0

