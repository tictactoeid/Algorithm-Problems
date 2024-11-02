# Median of Two Sorted Arrays
# Hard

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)  # m >= n

        target_length = (m + n) // 2

        low = 0
        high = n

        while low <= high:
            mid = (low + high) // 2
            j = mid
            i = target_length - j
            # consider nums2[0:j] with j elements and nums1[0:i] with i elements.

            AL = nums1[i - 1] if i > 0 else -math.inf
            BL = nums2[j - 1] if j > 0 else -math.inf

            AR = nums1[i] if i < m else math.inf
            BR = nums2[j] if j < n else math.inf

            if AL <= BR and BL <= AR:
                # valid
                if (m + n) % 2:  # odd
                    return min(AR, BR)
                else:  # even
                    return (min(AR, BR) + max(AL, BL)) / 2

            elif AL <= BR:
                # BL > AR. BL is too large!
                high = mid - 1
            else:
                low = mid + 1

