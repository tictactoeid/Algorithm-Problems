# Search in Rotated Sorted Array
# Medium

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:

            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            elif nums[low] < nums[mid]:
                # the left subarr is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # the right subarr is sorted
                if mid + 1 >= n:
                    return -1
                if nums[mid + 1] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
