# Maximum Value at a Given Index in a Bounded Array
# Medium

class Solution:
    def validate(self, value, n, index, maxSum) -> bool:
        count = 0
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1

        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value
        return count - value <= maxSum


    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low = 1
        high = maxSum
        answer = 0

        while low <= high:
            mid = (low + high) // 2
            if self.validate(mid, n, index, maxSum):
                answer = max(answer, mid)
                low = mid + 1
            else:
                high = mid - 1

        return answer
