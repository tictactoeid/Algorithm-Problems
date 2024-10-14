# Product of Array Except Self
# Medium

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]

        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]

        suffix[-1] = nums[-1]

        for i in range(n - 2, 0, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        answer = [0 for _ in range(n)]

        answer[0] = suffix[1]
        answer[n - 1] = prefix[n - 2]

        for i in range(1, n - 1):
            answer[i] = prefix[i - 1] * suffix[i + 1]

        return answer
