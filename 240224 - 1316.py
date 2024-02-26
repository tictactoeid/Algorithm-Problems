# 그룹 단어 체커
# 실버 5

n = int(input())
words = ['' for _ in range(n)]
count = 0
for i in range(n):
    words[i] = input()


def check(word):
    tmp = set()
    for i in range(len(word)):
        if (i == 0):
            tmp.add(word[i])
        elif (word[i - 1] == word[i]):
            continue
        elif word[i] in tmp:
            return False
        else:
            tmp.add(word[i])
    return True


for word in words:
    if check(word):
        count += 1

print(count)

