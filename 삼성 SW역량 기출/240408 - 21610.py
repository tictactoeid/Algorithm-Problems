# 마법사 상어와 비바라기
# 골드 5

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
mat_clouds = [[False for _ in range(n)] for _ in range(n)]


def rain():
    # (n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)에 비구름 생성
    return [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

def move(d, s, clouds: list):
    global mat_clouds
    dr = 0
    dc = 0

    if d == 1:
        dc -= 1
    elif d == 2:
        dr -= 1
        dc -= 1
    elif d == 3:
        dr -= 1
    elif d == 4:
        dr -= 1
        dc += 1
    elif d == 5:
        dc += 1
    elif d == 6:
        dr += 1
        dc += 1
    elif d == 7:
        dr += 1
    else:
        dr += 1
        dc -= 1
    dr *= s
    dc *= s

    for cloud in clouds:
        # 1. 이동
        cloud[0] = (cloud[0] + dr) % n
        cloud[1] = (cloud[1] + dc) % n
        # 2. 비
        mat[cloud[0]][cloud[1]] += 1
        mat_clouds[cloud[0]][cloud[1]] = True

    # 3. 구름 삭제
    new_clouds = []
    # 4. 물복사버그
    water_copy_bug(clouds)
    # 5. 구름 생성
    for i in range(n):
        for j in range(n):
            if mat[i][j] >= 2 and not mat_clouds[i][j]:
                new_clouds.append([i, j])
                mat[i][j] -= 2

    # 3. 구름 삭제
    mat_clouds = [[False for _ in range(n)] for _ in range(n)]

    return new_clouds


def water_copy_bug(regions):
    for region in regions:
        r = region[0]
        c = region[1]
        diagonals = [(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]
        count = 0
        for diagonal in diagonals:
            if 0 <= diagonal[0] < n and 0 <= diagonal[1] < n:
                if mat[diagonal[0]][diagonal[1]] > 0:
                    count += 1
        mat[r][c] += count
        # 물복사버그는 물이 없던 칸에 일어나지 않으므로,
        # 순차적으로 mat를 건드려도 영향이 없다


clouds = rain()
for i in range(m):
    d, s = map(int, input().split())
    clouds = move(d, s, clouds)

result = 0
for i in range(n):
    for j in range(n):
        result += mat[i][j]
print(result)