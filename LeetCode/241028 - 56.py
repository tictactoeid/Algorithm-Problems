# Merge Intervals
# Medium

class Solution:
    def overlap(self, interval1, interval2) -> bool:
        # assume interval1 <= interval2
        if interval1 > interval2:
            interval1, interval2 = interval2, interval1
        s1, e1 = interval1
        s2, e2 = interval2

        if e1 >= s2:
            return True

        return False

    def mergeTwo(self, interval1, interval2):
        s1, e1 = interval1
        s2, e2 = interval2
        return [min(s1, s2), max(e1, e2)]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        for interval in intervals:
            if not answer:
                answer.append(interval)
            else:
                answer.append(interval)
                if len(answer) > 1 and self.overlap(answer[-1], answer[-2]):
                    answer.append(self.mergeTwo(answer.pop(), answer.pop()))

        return answer
