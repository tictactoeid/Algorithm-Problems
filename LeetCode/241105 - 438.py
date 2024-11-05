# Find All Anagrams in a String
# Medium

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # O(n): iterate에 O(n), Counter 비교에 O(1) (Counter keys가 alphabet으로 한정되어 있으므로 O(26) = O(1)에 완료할 수 있다)
        if len(s) < len(p):
            return []

        n = len(p)
        p_counter = Counter(p)
        s_counter = Counter(s[:n])
        answer = []

        if p_counter == s_counter:
            answer.append(0)

        for i in range(0, len(s) - n):
            s_counter[s[i]] -= 1
            if not s_counter[s[i]]:
                del s_counter[s[i]]

            s_counter[s[i + n]] += 1

            if p_counter == s_counter:  # O(k): k <= 26으로 고정이므로 O(1)
                answer.append(i + 1)

        return answer
