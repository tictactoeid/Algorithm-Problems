# Best Time to Buy and Sell Stock II
# Medium


# Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                answer += prices[i + 1] - prices[i]

        return answer
