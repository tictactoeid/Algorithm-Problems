# Longest Substring Without Repeating Characters
# Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        start = 0
        end = 1
        answer = 0

        characters = {}
        repeated = set()

        characters[s[start]] = 1

        while start <= end and end <= n:
            if repeated:
                # start += 1
                characters[s[start]] -= 1
                if characters[s[start]] <= 1 and s[start] in repeated:
                    repeated.remove(s[start])
                start += 1
            else:
                # end += 1
                if not repeated:
                    answer = max(answer, end - start)

                if end == n:
                    break

                if s[end] in characters:
                    characters[s[end]] += 1
                else:
                    characters[s[end]] = 1
                if characters[s[end]] > 1:
                    repeated.add(s[end])
                end += 1

        return answer



