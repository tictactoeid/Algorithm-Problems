# 표 병합
# 레벨 3
# 2023 KAKAO BLIND RECRUITMENT

import sys

parents = [[(-1, -1) for _ in range(50)] for _ in range(50)]
table = [[None for _ in range(50)] for _ in range(50)]


def idx(x):
    return int(x) - 1


def union(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return
    parent1 = find(r1, c1)
    parent2 = find(r2, c2)

    value1 = get_value(r1, c1)
    value2 = get_value(r2, c2)

    if parent1 == parent2:
        return
    else:
        parents[parent2[0]][parent2[1]] = parent1

        if value1 is None and value2 is not None:
            set_value(r1, c1, value2)
        else:
            set_value(r1, c1, value1)


def find(r, c):
    parent = parents[r][c]
    if parent == (-1, -1) or parent == (r, c):
        return (r, c)
    else:
        parents[r][c] = find(parents[r][c][0], parents[r][c][1])
        return parents[r][c]


def get_value(r, c):
    parent = find(r, c)
    return table[parent[0]][parent[1]]


def set_value(r, c, value):
    parent = find(r, c)
    table[parent[0]][parent[1]] = value
    return value


def unmerge(r, c):
    lst = []
    target_parent = find(r, c)
    target_value = get_value(r, c)
    for i in range(50):
        for j in range(50):
            if find(i, j) == target_parent:
                lst.append((i, j))

    for target in lst:
        parents[target[0]][target[1]] = (-1, -1)
        table[target[0]][target[1]] = None

    table[r][c] = target_value


def solution(commands):
    global parents, table
    answer = []
    parents = [[(-1, -1) for _ in range(50)] for _ in range(50)]
    table = [[None for _ in range(50)] for _ in range(50)]
    for command in commands:
        cmd_list = command.split()
        if cmd_list[0] == "UPDATE":
            if len(cmd_list) == 4:
                # UPDATE r c value
                r, c = map(idx, cmd_list[1:3])
                value = cmd_list[3]
                set_value(r, c, value)
            else:
                value1 = cmd_list[1]
                value2 = cmd_list[2]
                for i in range(50):
                    for j in range(50):
                        if table[i][j] == value1:
                            table[i][j] = value2
                            # FIXME: get_value() and set_value()?
        elif cmd_list[0] == "MERGE":
            r1, c1, r2, c2 = map(idx, cmd_list[1:])
            union(r1, c1, r2, c2)
        elif cmd_list[0] == "UNMERGE":
            r, c = map(idx, cmd_list[1:])
            unmerge(r, c)
        else:  # PRINT
            r, c = map(idx, cmd_list[1:])
            value = get_value(r, c)
            if value is None:
                answer.append("EMPTY")
            else:
                answer.append(value)

    return answer

