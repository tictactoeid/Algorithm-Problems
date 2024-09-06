# 이진 검색 트리
# 골드 5

import sys
sys.setrecursionlimit(10**6)

# input: root - left - right
# output: left - right - root

prefix = []

while True:
    try:
        prefix.append(int(input()))
    except:
        break


def postfix(tree):
    if len(tree) == 0:
        return

    root = tree[0]
    if len(tree) == 1:
        print(root)
        return

    right = -1
    for i in range(1, len(tree)):
        if tree[i] > root:
            right = i
            break
    if right < 0:
        postfix(tree[1:])
        postfix([root])
    else:
        postfix(tree[1:right])
        postfix(tree[right:])
        postfix([root])


postfix(prefix)