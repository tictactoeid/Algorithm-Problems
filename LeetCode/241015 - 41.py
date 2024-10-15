# First Missing Positive
# Hard

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # filter useless elements
        nums = [nums[i] for i in range(n) if nums[i] > 0]

        # 1. nums 중간에 빈 원소가 있음 -> 1 ~ n
        # 2. nums 중간에 빈 원소가 없음 -> n+1
        # 즉 무조건 답은 1 ~ n+1임

        # nums = [3, 4, 1, 2]
        n = len(nums)

        for i in range(n):
            idx = abs(nums[i]) - 1  # list range를 맞추기 위해 -1하고, 나중에 +1
            if idx < n and nums[idx] > 0:
                nums[idx] *= -1  # mark as visited

        for i in range(n):
            if nums[i] > 0:  # not visited
                return i + 1  # 아까 index를 -1해서 구했으므로 답은 +1

        return n + 1


