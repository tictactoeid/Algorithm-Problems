# Restore The Array
# Hard

sys.set_int_max_str_digits(100000)  # ???????

class Solution:
    def helper(self, s, i, k):
        # s[i:] 에서, 앞에서부터 얼마까지 잘라야 k보다 작은지를 체크
        string = s[i:]
        low = 0
        high = min(len(string), len(str(k)))  # TLE 방지

        answer = low

        while low <= high:
            mid = (low + high) // 2
            if not string[:mid] or int(string[:mid]) <= k:
                answer = max(answer, mid)
                low = mid + 1
            else:
                high = mid - 1

        return answer + i


    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7

        n = len(s)
        dp = [0 for _ in range(n)]
        postfix_sum = [0 for _ in range(n+2)]
        postfix_sum[-1] = -1

        # 자기 자신에 대한 경우의 수를 세야

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif i == n-1:
                dp[-1] = 1 if int(s[-1]) <= k else 0
            else:  # i < n-1
                idx = self.helper(s, i, k)

                # if idx == n:
                #     # 자르지 않고 자기 자신만 들어가는 경우의 수 1
                #     # postfix_sum[n+1] = -1로 하여 간단히 처리
                #     value = postfix_sum[i+1] + 1
                # else:
                #     value = postfix_sum[i+1] - postfix_sum[idx+1]

                value = postfix_sum[i+1] - postfix_sum[idx+1]
                dp[i] = value % MOD
            postfix_sum[i] = (dp[i] + postfix_sum[i+1]) % MOD

        return dp[0]
