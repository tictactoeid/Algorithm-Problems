# 감시
# 골드 4

n, m = map(int, input().split())
mat = [[] for _ in range(n)]
cctv = []
direction_candidates = []
for i in range(n):
    mat[i] = list(map(int, input().split()))
    for j in range(m):
        if 0 < mat[i][j] < 6:
            cctv.append((i, j, mat[i][j]))
            if mat[i][j] == 2:
                direction_candidates.append(['H', 'V'])
            elif mat[i][j] == 1:
                direction_candidates.append(['N', 'S', 'E', 'W'])
            elif mat[i][j] == 3:
                direction_candidates.append(['NE', 'ES', 'SW', 'WN'])
            elif mat[i][j] == 4:
                direction_candidates.append(['WNE', 'NES', 'ESW', 'SWN'])
            else:
                direction_candidates.append([''])

# TODO: loop로 방향 정하기

