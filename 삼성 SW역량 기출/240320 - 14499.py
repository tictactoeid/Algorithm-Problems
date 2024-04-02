# 주사위 굴리기
# 골드 4

n, m, x, y, k = map(int, input().split())

matrix = [[] for _ in range(n)]

for i in range(n):
    matrix[i] = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
# 위 0 앞 1 아래 2 뒤 3 왼쪽 4 오른쪽 5


def roll(order):
    # 주사위 현재 x, y, 명령 (1234)
    global dice, x, y

    if order == 1:
        # 동쪽
        new_x = x
        new_y = y+1
        if new_y >= m:
            return -1

        new_dice = [dice[4], dice[1], dice[5], dice[3], dice[2], dice[0]]
        # 앞 뒤는 그대로
        # 위 - 오 - 아래 - 왼 한칸씩 시계방향으로 rotate
        # 위 -> 오
        # 오 -> 아래
        # 아래 -> 왼
        # 왼 -> 위
    elif order == 2:
        # 서쪽
        new_x = x
        new_y = y-1
        if new_y < 0:
            return -1

        new_dice = [dice[5], dice[1], dice[4], dice[3], dice[0], dice[2]]
        # 위 - 오 - 아래 - 왼 반시계
        # 위 0 앞 1 아래 2 뒤 3 왼쪽 4 오른쪽 5
        # 위 0 <- 오 5
        # 오 5 <- 아래 2
        # 아래 2 <- 왼4
        # 왼 4 <- 위0
    elif order == 3:
        # 북쪽
        new_x = x - 1
        new_y = y
        if new_x < 0:
            return -1
        new_dice = [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]
        # 위 - 앞 - 아래 - 뒤 반시계
        # 위 0 <- 앞 1
        # 앞 1 <- 아래 2
        # 아래 2 <- 뒤 3
        # 뒤 3 <- 위 0
    else:
        # 남쪽
        new_x = x + 1
        new_y = y
        if new_x >= n:
            return -1
        new_dice = [dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]]

    cp = matrix[new_x][new_y]
    if cp != 0:
        new_dice[2] = cp
        matrix[new_x][new_y] = 0
    else:
        matrix[new_x][new_y] = new_dice[2]
    x = new_x
    y = new_y
    dice = new_dice
    return new_dice[0]


orders = list(map(int, input().split()))
for order in orders:
    result = roll(order)
    if result >= 0:
        print(result)
