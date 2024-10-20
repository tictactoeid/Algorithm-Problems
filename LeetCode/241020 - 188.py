# Best Time to Buy and Sell Stock IV
# Hard

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        reset = [-math.inf] * k  # before jth transaction
        hold = [-math.inf] * k  # holding jth stock
        reset[0] = 0

        # buy: reset[j] -> hold[j]
        # sell: hold[j-1] -> reset[j], hold[k-1] -> RETURN
        # stay: hold[j] -> hold[j], reset[j] -> reset[j]
        n = len(prices)
        answer = 0

        for i in range(n):
            for j in range(k):
                hold[j] = max(reset[j] - prices[i], hold[j])
                if j > 0:
                    reset[j] = max(reset[j], hold[j-1] + prices[i])
                answer = max(answer, hold[j] + prices[i], reset[j]) # hold[k-1] 이후 한 번 더 판매할 수 있음에 유의
                # 헷갈리면 reset을 (k+1) 길이로 해도 됨
            #print(hold, reset)
        return answer
