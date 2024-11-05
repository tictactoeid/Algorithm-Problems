# Subsets
# Medium

class Solution:
    def helper(self, idx, subset):
        if idx == self.n:
            self.answer.append(subset)
            return

        self.helper(idx + 1, subset)
        self.helper(idx + 1, subset + [self.nums[idx]])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.n = len(nums)
        self.answer = []
        self.helper(0, [])
        return self.answer
    