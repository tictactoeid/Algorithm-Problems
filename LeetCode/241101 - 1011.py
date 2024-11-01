# Capacity To Ship Packages Within D Days
# Medium

class Solution:
    def is_capable(self, capacity, weights, days):
        pos = 0
        current_weight = 0
        current_day = 0

        while pos < len(weights):
            if weights[pos] > capacity:
                return False
            if current_weight + weights[pos] > capacity:
                current_day += 1
                current_weight = 0
                continue
            else:
                current_weight += weights[pos]
                pos += 1

        if current_weight:
            current_day += 1

        if current_day <= days:
            return True
        else:
            return False

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        capacity = 0
        # O(n logk)
        # print(self.is_capable(14, weights, days))

        low = max(weights)
        high = sum(weights)
        answer = math.inf

        while low <= high:  # O(logk)
            mid = (low + high) // 2
            if self.is_capable(mid, weights, days):  # O(n)
                answer = min(answer, mid)
                high = mid - 1
                # print(low, high, mid)
            else:
                low = mid + 1
        return answer
