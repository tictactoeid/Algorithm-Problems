# Wiggle Sort II
# Medium

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # O(nlogn)
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1, 2, 3, 4, 5, 6]
        # [1, 2, 3] 과 [4, 5, 6]으로 나눔
        # 뒤에서부터 순서대로 채움: [3, 2, 1] 과 [6, 5, 4]를 합쳐 [3, 6, 2, 5, 1, 4]
        # 뒤에서부터 채우는 이유는 중복 원소를 처리하기 위해서임

        # [1, 2, 3, 4, 5]
        # [1, 5, 2, 4, 3]
        tmp = sorted(nums)
        n = len(nums)
        x = (n + 1) // 2

        start = n - 1 if n % 2 else n - 2
        for i in range(start, -1, -2):
            nums[i] = tmp[(start - i) // 2]

        start = n - 2 if n % 2 else n - 1
        for i in range(start, 0, -2):
            nums[i] = tmp[(start - i) // 2 + x]



