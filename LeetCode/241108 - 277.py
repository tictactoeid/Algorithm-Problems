# Find the Celebrity
# Medium

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity_1(self, n: int) -> int:
        # Approach 1
        possible = [True for _ in range(n)]

        for i in range(n):
            if not possible[i]:
                continue
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    # i knows j
                    possible[i] = False
                else:
                    possible[j] = False
        # print(possible)
        for i in range(n):
            if possible[i]:
                for j in range(n):
                    if i == j:
                        continue
                    if not knows(j, i):
                        possible[i] = False
                        break
            if possible[i]:
                return i

        return -1

    def findCelebrity(self, n: int) -> int:

        candidate = 0
        for i in range(1, n):
            if not knows(i, candidate):
                candidate = i
            elif knows(candidate, i):
                candidate = i

        for i in range(n):
            if i == candidate:
                continue
            if not knows(i, candidate) or knows(candidate, i):
                return -1
        return candidate
