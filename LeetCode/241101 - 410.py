# Split Array Largest Sum
# Hard

# O(nlogk)
class Solution:
    def validate(self, nums, k, x):
        pos = 0
        pieces = 0
        curr_sum = 0
        while pos < len(nums):
            if nums[pos] > x:
                return False
            if curr_sum + nums[pos] > x:
                curr_sum = 0
                pieces += 1
                continue
            curr_sum += nums[pos]
            pos += 1

        if curr_sum:
            pieces += 1

        if pieces <= k:
            return True
        else:
            return False

    def splitArray(self, nums: List[int], k: int) -> int:
        # 모든 subarray의 sum이 x 이하가 되도록 자르자

        # x가 너무 작으면 -> 조각의 수가 k보다 많아짐
        # x가 너무 크면 -> 조각의 수가 k보다 적거나 같아짐
        # 조각의 수 <= k인 x 중 최솟값 을 찾으면 될 듯
        # 조각의 수 < k이면, 조각을 더 잘게 잘라서 조건 (모든 sum <= x)을 만족하면서 k개로 자를 수 있으므로 True를 return

        answer = math.inf
        high = sum(nums)
        low = 0

        while low <= high:
            mid = (low + high) // 2
            # print(low, high)
            if self.validate(nums, k, mid):
                answer = min(answer, mid)
                high = mid - 1
            else:
                low = mid + 1
        return answer
