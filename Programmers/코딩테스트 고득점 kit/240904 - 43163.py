# 단어 변환
# 레벨 3
# DFS / BFS

from collections import deque


def changeable(current, target):
    flag = False
    for i in range(len(current)):
        if current[i] != target[i]:
            if flag:
                return False
            flag = True
    return True


def solution(begin, target, words):
    answer = 0

    visited = [False for _ in range(len(words))]

    if target not in words:
        return 0

    q = deque()
    q.append((-1, 0))
    while q:
        idx, dist = q.popleft()
        if idx == -1:
            word = begin
        else:
            word = words[idx]
            visited[idx] = True
        # TODO: visited 설정을 위해 index로 변경?
        for i in range(len(words)):
            if not visited[i] and changeable(word, words[i]):
                if words[i] == target:
                    return dist + 1
                q.append((i, dist + 1))

    return 0


print(solution("hit", "cog",	["hot", "dot", "dog", "lot", "log", "cog"]))
