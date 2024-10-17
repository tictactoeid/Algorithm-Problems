# Find Minimum in Rotated Sorted Array
# Medium

# Binary Search와 유사
# 약간 더 많은 경우의 수를 고려하면 됨

class Solution:
    def search(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        idx = n // 2

        if (idx == 0 or nums[idx - 1] > nums[idx]) and (idx == n - 1 or nums[idx] < nums[idx + 1]):
            return nums[idx]
        else:
            list1 = nums[:idx]
            list2 = nums[idx + 1:]
            if len(list1) == 0:
                return self.search(list2)
            elif len(list2) == 0:
                return self.search(list1)
            else:
                if list1[0] < list2[0] and list1[-1] < list2[-1]:
                    return self.search(list1)  # TODO
                elif list1[0] > list2[0] and list1[-1] > list2[-1]:
                    return self.search(list2)
                elif list1[0] < list2[0] and list1[-1] > list2[-1]:
                    return self.search(list2)
                else:
                    return self.search(list1)

    def findMin(self, nums: List[int]) -> int:
        return self.search(nums)
