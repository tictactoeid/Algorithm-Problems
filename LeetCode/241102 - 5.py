# Longest Palindromic Substring
# Medium

class Solution:
    def expand(self, i, j, s, n):
        while i >= 0 and j < n:
            if s[i] != s[j]:
                break
            candidate = s[i:j + 1]
            if len(s[i:j + 1]) > len(self.answer):
                self.answer = s[i:j + 1]
            i -= 1
            j += 1

    def longestPalindrome(self, s: str) -> str:
        # dp[i][j]: s[i:j+1] is palindrome?
        n = len(s)

        self.answer = s[0]

        for x in range(n):
            self.expand(x, x, s, n)  # even length case
            self.expand(x - 1, x, s, n)  # odd length case

        # print(dp)
        return self.answer

