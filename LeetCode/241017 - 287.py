# Find the Duplicate Number
# Medium

class Solution:
    def findDuplicate_bit(self, nums: List[int]) -> int:
        bit = 0
        for num in nums:
            mask = 1 << num
            if bit & mask:
                return num
            bit |= mask

    def findDuplicate_floyd(self, nums: List[int]) -> int:
        # Floyd's Cycle Detection
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:  # cycle detected
                break

        # the entrace of the cycle is the answer.

        slow = nums[0]  # reset the slow pointer
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) time and O(1) memory
        # but it modifies the array

        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            else:
                nums[idx] = -nums[idx]
