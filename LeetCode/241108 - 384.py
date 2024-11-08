# Shuffle an Array
# Medium

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.origin = list(nums)
        self.n = len(nums)

    def reset(self) -> List[int]:
        self.nums = list(self.origin)
        return self.nums

    def _shuffle(self, i):
        if i == self.n - 1:
            return
        idx = random.randint(i, self.n - 1)
        self.nums[idx], self.nums[i] = self.nums[i], self.nums[idx]
        return self._shuffle(i + 1)

    def shuffle(self) -> List[int]:
        self._shuffle(0)
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
