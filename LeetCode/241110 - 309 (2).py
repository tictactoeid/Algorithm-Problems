# Best Time to Buy and Sell Stock with Cooldown
# Medium

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        default = 0
        hold = -prices[0]
        cooldown = -math.inf

        for i in range(1, len(prices)):
            price = prices[i]

            before_hold = hold

            hold = max(before_hold, default - price)
            default = max(default, cooldown)
            cooldown = before_hold + price

        return max(hold, default, cooldown)

