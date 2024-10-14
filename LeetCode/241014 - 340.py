# Longest Substring with At Most K Distinct Characters
# Medium

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        start = 0
        end = 1  # consider s[start:end].
        count = {}  # {char: count}, e. g. count["a"] = 2
        count[s[start]] = 1

        answer = 0

        while start <= end and end <= n:
            if len(count) <= k:
                answer = max(answer, end - start)
                if end < n:
                    if s[end] not in count:
                        count[s[end]] = 0
                    count[s[end]] += 1

                end += 1

            else:
                count[s[start]] -= 1
                if not count[s[start]]:
                    count.pop(s[start])
                start += 1

        return answer

