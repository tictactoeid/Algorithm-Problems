# 다각형의 면적
# 골드 5

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]


# 신발끈 공식
def sol1(points):
    result = 0
    for i in range(n-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        result += 0.5 * (x1 * y2 - y1 * x2)

    x1, y1 = points[n-1]
    x2, y2 = points[0]
    result += 0.5 * (x1 * y2 - y1 * x2)
    print(abs(round(result, 1)))


# 모든 선분 적분의 합
def sol2(points):
    result = 0
    for i in range(n - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        result += 0.5 * (x2 - x1) * (y2 + y1)

    x1, y1 = points[n - 1]
    x2, y2 = points[0]
    result += 0.5 * (x2 - x1) * (y2 + y1)
    print(abs(round(result, 1)))


#sol1(points)
sol2(points)
