# Remove Duplicates from Sorted Array II
# Medium
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        while i < len(nums):
            if nums[i] == nums[i - 1] and nums[i - 1] == nums[i - 2]:
                del nums[i]
            else:
                i += 1
        print(nums)
        return len(nums)

Solution().removeDuplicates(nums=[1, 1, 1, 2, 3])
