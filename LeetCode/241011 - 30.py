# Substring with Concatenation of All Words
# Hard

# set이나 list sort 후 bisect일 줄 알았는데
# 중복 처리를 위해 dict를 사용해야 하는 문제

from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        total_len = word_len * len(words)
        answer = []

        words = Counter(words)
        # print(words)

        for i in range(0, len(s) - total_len + 1):
            idx = i
            current_words_count = defaultdict(int)
            flag = False
            while idx < i + total_len:
                target_word = s[idx:idx + word_len]
                current_words_count[target_word] += 1
                if current_words_count[target_word] > words[target_word]:
                    flag = True
                    # print(i, current_words_count)

                    break
                idx += word_len
            if not flag:
                answer.append(i)

        return answer


