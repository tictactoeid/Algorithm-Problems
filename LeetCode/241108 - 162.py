# Find Peak Element
# Medium

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            left = nums[mid - 1] if mid > 0 else -math.inf
            right = nums[mid + 1] if mid < n - 1 else -math.inf

            if left < nums[mid] and nums[mid] > right:
                return mid
            elif left < nums[mid] < right:
                low = mid + 1
            else:
                high = mid - 1
