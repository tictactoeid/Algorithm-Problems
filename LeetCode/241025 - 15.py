# 3Sum
# Medium

class Solution:
    def threeSum_tle(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = set()

        for i in range(n):
            for j in range(i + 1, n):
                target = -nums[i] - nums[j]
                idx = bisect.bisect_left(nums[j + 1:], target)
                if idx + j + 1 < n and nums[idx + j + 1] == target:
                    tmp = (nums[i], nums[j], target)
                    answer.add(tmp)

        result = []
        for x, y, z in answer:
            result.append([x, y, z])

        return result

    def threeSum(self, nums):
        nums.sort()
        n = len(nums)

        fixed = 0
        low = 1
        high = 2
        answer = []
        ans = set()

        while fixed <= n - 3:
            target = -nums[fixed]
            low = fixed + 1
            high = n - 1
            while low < high:
                # print(fixed, low, high)
                value = nums[low] + nums[high]

                if value == target:
                    # answer.append([nums[fixed], nums[low], nums[high]])
                    ans.add((nums[fixed], nums[low], nums[high]))
                    low += 1
                    high -= 1
                elif value < target:
                    low += 1
                else:
                    high -= 1

                # if value > target:
                #     #tmp = nums[low]
                #     #while low < high and nums[low] == tmp:
                #     low += 1
                #     high = low+1
                # else:
                #     if value == target:
                #         if (nums[fixed], nums[low], nums[high]) not in ansset:
                #             ansset.add((nums[fixed], nums[low], nums[high]))
                #             answer.append([nums[fixed], nums[low], nums[high]])
                #     #tmp = nums[high]
                #     #while high < n and nums[high] == tmp:
                #     high += 1
            fixed += 1

        answer = [[x, y, z] for x, y, z in ans]

        return answer



