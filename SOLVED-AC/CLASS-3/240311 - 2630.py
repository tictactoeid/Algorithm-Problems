# 색종이 만들기
# 실버 2

n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    matrix[i] = list(map(int, input().split()))


def cut(startX, startY, endX, endY):
    # start <= i, j < end, matrix[i][j]
    # recursive

    if endX - startX == 1:
        if matrix[startY][startX] == 0:
            return 1, 0 # white, blue
        else:
            return 0, 1

    blueFlag = False
    whiteFlag = False
    for i in range(startY, endY):
        if not blueFlag and 1 in matrix[i][startX:endX]:
            blueFlag = True
        if not whiteFlag and 0 in matrix[i][startX:endX]:
            whiteFlag = True
        if blueFlag and whiteFlag:
            half = (endX - startX) // 2
            return tuple(sum(elem) for elem in zip(
                cut(startX, startY, startX + half, startY + half),
                cut(startX + half, startY + half, endX, endY),
                cut(startX + half, startY, endX, startY + half),
                cut(startX, startY + half, startX + half, endY)
            ))

    if blueFlag:
        return 0, 1
    else:
        return 1, 0

white, blue = cut(0, 0, n, n)
print(white)
print(blue)