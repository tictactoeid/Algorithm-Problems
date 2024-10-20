# Best Time to Buy and Sell Stock III
# Hard

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state
        # reset[0], reset[1], hold[0], hold[1]
        # 각각 1, 2번째 transaction을 의미
        # timeline
        # 시작 (reset[0]) - 첫 구매 (hold[0]) - 판매 (reset[1]) - 두 번째 구매 (hold[1]) - 판매 (reset[2])

        # 1번째 transaction
        # 구매: reset[0] -> hold[0]
        # 유지: hold[0] -> hold[0] / reset[0] -> reset[0]
        # 판매: hold[0] -> reset[1]
        # 2번째 transaction
        # 구매: reset[1] -> hold[1]
        # 유지: hold[1] -> hold[1] / reset[1] -> reset[1]
        # 판매: hold[1] -> RETURN
        n = len(prices)
        reset = [0, -math.inf]
        hold = [-math.inf, -math.inf]
        answer = 0
        for i in range(n):
            next_reset = [reset[0], reset[1]]
            next_hold = [hold[0], hold[1]]

            next_hold[0] = max(hold[0], reset[0] - prices[i])
            next_reset[1] = max(reset[1], hold[0] + prices[i])

            next_hold[1] = max(hold[1], reset[1] - prices[i])
            answer = max(next_hold[1] + prices[i], answer, next_reset[1])  # 2번째 거래를 안 할 수도

            hold = next_hold
            reset = next_reset
            # print(hold, reset)

        return answer
