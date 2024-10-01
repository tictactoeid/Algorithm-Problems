# N-Queen
# 골드 4

n = int(input())
result = 0

queens = [-1 for _ in range(n)]
# queens[i] = j -> mat[i][j]에 queen 위치


def backtracking(row=0, count=0):
    global result
    if count == n:
        result += 1
        return

    if n - row < n - count:
        # 남은 row에 퀸을 하나씩 배치해도 절대 n개를 채울 수 없음
        #print("x")
        return

    for col in range(n):
        if col in queens:
            continue

        flag = False
        for queen_row in range(row):
            queen_col = queens[queen_row]
            if abs(queen_row - row) == abs(queen_col - col):
                flag = True
                break
        if flag:
            continue

        queens[row] = col
        backtracking(row+1, count+1)
        queens[row] = -1


#backtracking(arr, 0, 0)
backtracking(0)
print(result)
