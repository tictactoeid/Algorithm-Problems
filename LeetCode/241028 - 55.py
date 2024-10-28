# Jump Game
# Medium

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        maximum = nums[0]
        n = len(nums)

        for i in range(n):
            if maximum < i:
                return False

            maximum = max(maximum, nums[i] + i)
            if maximum >= n - 1:
                return True

        return False

