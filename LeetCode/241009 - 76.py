# Minimum Window Substring
# Hard
class Solution:
    result = ""
    t = ""
    characters = {}

    def init_characters(self, t: str) -> None:
        self.result = ""
        self.t = t
        self.characters = {}
        for x in t:
            if x in self.characters.keys():
                self.characters[x] += 1
            else:
                self.characters[x] = 1

    def covered(self, current_chars: dict) -> bool:
        for char in self.characters.keys():
            try:
                if current_chars[char] < self.characters[char]:
                    return False
            except KeyError:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        self.init_characters(t)

        start = 0
        end = 1
        current_chars = {s[start]: 1}
        while start <= end and end <= len(s):
            current = s[start:end]

            if self.covered(current_chars):
                if not self.result or len(self.result) > len(current):
                    self.result = current

                current_chars[s[start]] -= 1
                start += 1
            else:
                if end < len(s):
                    if s[end] in current_chars.keys():
                        current_chars[s[end]] += 1
                    else:
                        current_chars[s[end]] = 1
                end += 1

        return self.result
