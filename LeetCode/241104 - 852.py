# Peak Index in a Mountain Array
# Medium

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # increase and decrease strictly..?

        n = len(arr)
        low = 1
        high = n - 2

        while low <= high:
            mid = (low + high) // 2
            left_val = arr[mid - 1] if mid > 0 else +math.inf
            right_val = arr[mid + 1] if mid < n - 1 else -math.inf

            if left_val < arr[mid] and arr[mid] > right_val:
                return mid

            if left_val < arr[mid] < right_val:
                low = mid + 1
            else:
                high = mid - 1

