# Find First and Last Position of Element in Sorted Array
# Medium

class Solution:
    def searchRange_bisect(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        n = len(nums)

        if left > n - 1 or nums[left] != target:
            left = -1
        if right - 1 > n - 1 or right - 1 < 0 or nums[right - 1] != target:
            right = -1
        else:
            right -= 1
        return [left, right]

    def search(self, nums, target, low, high, right=False):
        if low > high:
            return -1
        if low == high:
            if target == nums[low]:
                return low
            else:
                return -1

        mid = (low + high) // 2
        if nums[mid] == target:
            if right and mid < len(nums) - 1 and nums[mid + 1] == target:
                return self.search(nums, target, mid + 1, high, right)
            elif not right and mid > 0 and nums[mid - 1] == target:
                return self.search(nums, target, low, mid - 1, right)
            return mid  # TODO consider left or right
        elif nums[mid] > target:
            return self.search(nums, target, low, mid - 1, right)
        else:
            return self.search(nums, target, mid + 1, high, right)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # print(self.search([1, 2, 2, 2, 3, 4, 5], 2, 0, 4, True))
        return [self.search(nums, target, 0, len(nums) - 1, False), self.search(nums, target, 0, len(nums) - 1, True)]
