# Find the Longest Valid Obstacle Course at Each Position
# Hard

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        tmp = []
        answer = []
        n = len(obstacles)
        for i in range(n):
            idx = bisect.bisect_right(tmp, obstacles[i])
            if idx >= len(tmp):
                tmp.append(obstacles[i])
            else:
                tmp[idx] = obstacles[i]
            answer.append(idx + 1)
        return answer
