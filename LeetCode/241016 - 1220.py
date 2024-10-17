# Count Vowels Permutation
# Hard (??)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = 0
        e = 1
        i = 2
        o = 3
        u = 4

        modulo_operand = 10 ** 9 + 7

        dp = [[0 for _ in range(5)] for _ in range(n)]

        dp[0] = [1, 1, 1, 1, 1]

        for idx in range(1, n):
            dp[idx][a] = (dp[idx - 1][e] + dp[idx - 1][i] + dp[idx - 1][u]) % modulo_operand
            dp[idx][e] = (dp[idx - 1][a] + dp[idx - 1][i]) % modulo_operand
            dp[idx][i] = (dp[idx - 1][e] + dp[idx - 1][o]) % modulo_operand
            dp[idx][o] = dp[idx - 1][i] % modulo_operand
            dp[idx][u] = (dp[idx - 1][i] + dp[idx - 1][o]) % modulo_operand

        return sum(dp[-1]) % modulo_operand

        #
        # io, iu
        # ou

        # ea, ia, ua
        # ae, ie
        # ei, oi
        # io
        # iu, ou