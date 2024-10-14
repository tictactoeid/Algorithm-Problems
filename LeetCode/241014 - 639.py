# Decode Ways II
# Hard

# 아이디어 자체는 간단한 dp이지만
# 고려해야 할 경우의 수가 아주 많았던 문제

class Solution:
    modulo_operand = 10 ** 9 + 7

    def numDecodings(self, s: str) -> int:
        n = len(s)
        Z = 26
        dp = [0 for _ in range(n + 1)]

        # dp[i]: s[0:i]에 대한 decode 경우의 수
        dp[0] = 1
        if s[0] == "*":
            dp[1] = 9  # 1 to 9
        elif 1 <= int(s[0]) <= 9:
            dp[1] = 1  # must be valid?
        else:
            dp[1] = 0

        # *
        # 1*
        # 2*
        # **

        # *1, ... *6
        # *7, ... *9

        for i in range(2, n + 1):
            prev = s[i - 1]
            prev_prev = s[i - 2]  # if i >= 2 else ""
            if prev != "*" and prev_prev != "*":
                if 10 <= int(prev_prev + prev) <= Z:
                    if 1 <= int(prev) <= 9:
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 2]
                elif 1 <= int(prev) <= 9:
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = 0

                dp[i] %= self.modulo_operand

            elif prev == "*" and prev_prev != "*":
                # 1*, 2*
                dp[i] = dp[i - 1] * 9

                if s[i - 2] == "1":  # 11, 12, ..., 19
                    dp[i] += dp[i - 2] * 9
                elif s[i - 2] == "2":  # 21, ..., 26
                    dp[i] += dp[i - 2] * 6
                else:  # 0*, 3*, 4*, ..., 9* are invalid
                    pass

                dp[i] %= self.modulo_operand

            elif prev != "*" and prev_prev == "*":
                # *0
                # *1, ... *6
                # *7, ... *9

                if prev == "0":
                    # 10, 20 is valid
                    # ... / 0 is invalid
                    dp[i] = dp[i - 2] * 2
                elif 1 <= int(prev) <= 6:
                    dp[i] = dp[i - 1] + dp[i - 2] * 2
                else:  # 7, 8, 9
                    # 17, 18, 19
                    dp[i] = dp[i - 1] + dp[i - 2]

                dp[i] %= self.modulo_operand

            else:
                # **
                dp[i] = dp[i - 2] * (26 - 10 + 1 - 2)
                # 10 to 26, exclude 10 and 20

                dp[i] += dp[i - 1] * 9

                dp[i] %= self.modulo_operand

        #print(dp)
        return dp[n]
