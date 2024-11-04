# Remove Covered Intervals
# Medium

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        stack = []
        count = 0

        for i, interval in enumerate(intervals):
            start, end = interval

            while stack and stack[-1] < end:
                stack.pop()
            if stack:
                count += 1
            stack.append(end)

        return n - count
