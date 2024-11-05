# Find Right Interval
# Medium

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted([(interval[0], i) for i, interval in enumerate(intervals)])
        n = len(intervals)
        answer = [-1 for _ in range(n)]

        for i, interval in enumerate(intervals):
            start, end = interval
            idx = bisect.bisect_left(starts, (end, 0))
            if idx >= n:
                continue
            answer[i] = starts[idx][1]
        return answer
