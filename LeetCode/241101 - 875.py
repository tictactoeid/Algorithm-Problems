# Koko Eating Bananas
# Medium

class Solution:
    def can_eat(self, k, piles, h):
        hour = 0
        if k == 0:
            return False

        for pile in piles:
            hour += math.ceil(pile / k)

        if hour <= h:
            return True
        else:
            return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = math.inf
        low = 0
        high = max(piles)
        answer = math.inf

        while low <= high:
            mid = (low + high) // 2
            if self.can_eat(mid, piles, h):
                answer = min(answer, mid)
                high = mid - 1
            else:
                low = mid + 1
        return answer
