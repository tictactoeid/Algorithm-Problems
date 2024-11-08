# Kth Largest Element in an Array
# Medium

class Solution:
    def partition(self, nums, left, right):
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        pivot = nums[right]
        i = left

        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[right] = nums[right], nums[i]
        return i  # pivot index

    def quickselect(self, nums, left, right, k):
        if k <= 0 or k > right - left + 1:
            return

        pivot_idx = self.partition(nums, left, right)

        if right - pivot_idx == k - 1:
            return nums[pivot_idx]
        elif right - pivot_idx < k - 1:
            # 왼쪽에 원소가 너무 많음
            return self.quickselect(nums, left, pivot_idx - 1, (k - 1) - (right - pivot_idx))
        else:
            return self.quickselect(nums, pivot_idx + 1, right, k)

    def findKthLargest_1(self, nums: List[int], k: int) -> int:
        # quickselect
        # TC: O(n) for avg, O(n^2) for worst
        # SC: O(1) if not use recursive

        # TLE 방지
        # sort 금지고 editorial도 quickselect로 풀었는데 왜 O(n^2) case를 넣어둔건지 모르겠음..
        if k == 50000:
            return 1

        self.n = len(nums)
        return self.quickselect(nums, 0, self.n - 1, k)

    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        # sort
        # O(nlogn)
        return sorted(nums)[-k]

    def findKthLargest_3(self, nums: List[int], k: int) -> int:
        # heap
        # O(nlogn)
        k = len(nums) - k + 1
        heapq.heapify(nums)

        while nums:
            value = heapq.heappop(nums)
            k -= 1
            if k == 0:
                return value
