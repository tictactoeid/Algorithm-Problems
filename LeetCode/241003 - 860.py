# Maximum Product Subarray
# Hard

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        strs = list(map(str, nums))
        strs.sort(reverse=True, key=lambda x: x * 10)
        s = ""
        for x in strs:
            s += x
        s = s.lstrip("0")
        if not s:
            return '0'
        return s


print(Solution().largestNumber(["0", "0"]))