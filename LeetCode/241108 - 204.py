# Count Primes
# Medium

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0

        prime = [True for _ in range(n)]
        prime[0] = False
        prime[1] = False
        count = 0
        for i in range(2, n):
            if not prime[i]:
                continue
            count += 1
            x = i * 2
            while x <= n-1:
                prime[x] = False
                x += i

        return count
