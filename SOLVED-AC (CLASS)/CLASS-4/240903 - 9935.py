# 문자열 폭발
# 골드 4

from collections import deque

# input: abcd
# s1: [a b c d]
# b c

# [a b c] d []
# [a b c] [d]
# [a b] c [d]
# [a ] b [c d] => boom
# [a] [d]
# [] a [d]
# [] [a d] => end


def simple(string, bomb):
    f = string.find(bomb)
    while f != -1:
        string = string[:f] + string[f+len(bomb):]
        f = string.find(bomb)

    print(string)


string = input()
bomb = input()

s1 = deque()
s2 = deque()

for x in string:
    s1.appendleft(x)



while s1:
    char = s1.popleft()
    flag = False
    if char == bomb[0]:
        for j in range(1, len(bomb)):
            try:
                if s2[j-1] != bomb[j]:
                    break
            except IndexError:
                break
            if j == len(bomb)-1:
                flag = True
                break
        if len(bomb) == 1:
            # just remove char.
            continue
        elif flag:
            for _ in range(len(bomb) - 1):
                s2.popleft()
        else:
            s2.appendleft(char)
    else:
        s2.appendleft(char)
    #print(f"s1: {s1} s2: {s2}")

if s2:
    print(''.join(s2))

else:
    print("FRULA")

a = deque(['a', 'b', 'c'])