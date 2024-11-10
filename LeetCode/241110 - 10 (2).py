# Regular Expression Matching
# Hard

class Solution:
    def dp(self, string, pattern):
        if not string and not pattern:
            return True
        if string and not pattern:
            return False

        if len(pattern) > 1 and pattern[1] == "*":
            if not string:
                return self.dp(string, pattern[2:])
            elif pattern[0] == ".":
                value = False
                for i in range(len(string) + 1):
                    value = value or self.dp(string[i:], pattern[2:])
                    if value:
                        break
                return value
            else:
                value = self.dp(string, pattern[2:])
                for i in range(len(string) + 1):
                    if i == len(string):
                        value = value or self.dp("", pattern[2:])
                    elif pattern[0] == string[i]:
                        value = value or self.dp(string[i + 1:], pattern[2:])
                        if value:
                            break
                    else:
                        break
                return value

        else:
            if not string:
                return False
            return (pattern[0] == string[0] or pattern[0] == ".") and self.dp(string[1:], pattern[1:])

    def isMatch(self, s: str, p: str) -> bool:
        return self.dp(s, p)
