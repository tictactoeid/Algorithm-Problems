# 암호 만들기
# 골드 5
# 재활훈련 - 백트래킹

l, c = map(int, input().split())
alphabets = sorted(list(input().split()))


def backtrack(code, leftovers):
    if len(code) == l:
        print_code(code)
        return

    for i in range(len(leftovers)):
        backtrack(code + leftovers[i], leftovers[i+1:])


def print_code(code):
    aeiou = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    flag = False

    for x in code:
        if x in aeiou:
            flag = True
        else:
            cnt += 1

    if flag and cnt > 1:
        print(code)


backtrack("", alphabets)
