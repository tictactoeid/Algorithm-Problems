# 게리맨더링 2
# 골드 3
import math

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
total = sum(sum(mat[x]) for x in range(n))

def set_boundary(x, y, d1, d2):
    boundary = [[0 for _ in range(n)] for _ in range(n)]

    j = y
    for i in range(x, x+d1+1):
        boundary[i][j] = 5
        j -= 1

    j = y
    for i in range(x, x+d2+1):
        boundary[i][j] = 5
        j += 1

    j = y-d1
    for i in range(x+d1, x+d1+d2+1):
        boundary[i][j] = 5
        j += 1

    j = y+d2
    for i in range(x+d2, x+d2+d1+1):
        boundary[i][j] = 5
        j -= 1

    # for i in range(n):
    #     for j in range(n):
    #         print(boundary[i][j], end=' ')
    #     print()
    # print()
    return boundary


def population(x, y, d1, d2):
    global n
    boundary = set_boundary(x, y, d1, d2)
    population = [0, 0, 0, 0, 0]


    for r in range(0, x+d1):
        for c in range(0, y+1):
            # region 1 or 5
            # 오른쪽 아래로 가다가 boundary 만나면 거기부터는 5번
            if boundary[r][c] == 5:
                break
            population[0] += mat[r][c]

    for r in range(x+d2+1):
        for c in range(n-1, y, -1):
            if boundary[r][c] == 5:
                break
            population[1] += mat[r][c]

    for r in range(x+d1, n):
        for c in range(y-d1+d2):
            if boundary[r][c] == 5:
                break
            population[2] += mat[r][c]

    for r in range(x+d2+1, n):
        for c in range(n-1, y-d1+d2-1, -1):
            if boundary[r][c] == 5:
                break
            population[3] += mat[r][c]

    population[4] = total - sum(population)
    # print(population)
    return max(population) - min(population)

# def population(x, y, d1, d2):
#     result = [0, 0, 0, 0, 0]
#     #new_mat = [[0 for _ in range(n)] for _ in range(n)]
#
#
#
#     for i in range(n):
#         for j in range(n):
#             region = get_region(i, j, x, y, d1, d2)
#             result[region-1] += mat[i][j]
#             #new_mat[i][j] = region
#             print(region, end=' ')
#         print()
#     print()
#     return max(result) - min(result)
#

minimum = math.inf
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if 0 <= x < x+d1+d2 < n and 0 <= y-d1 < y < y+d2 < n:
                    # print(population(x, y, d1, d2))
                    minimum = min(minimum, population(x, y, d1, d2))

print(minimum)
