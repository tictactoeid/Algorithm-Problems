# Sort Colors
# Medium

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(i, j):
            if i > j:
                return

            # find the first zero in the subarray
            for idx in range(i, j+1):
                if nums[idx] == 0:
                    # this is the first zero
                    nums[idx], nums[i] = nums[i], nums[idx]
                    return helper(i+1, j)

            # no zero in the subarray, now find the first two
            for idx in range(j, i-1, -1):
                if nums[idx] == 2:
                    # this is the first two.
                    nums[idx], nums[j] = nums[j], nums[idx]
                    return helper(i, j-1)

        helper(0, len(nums) - 1)
