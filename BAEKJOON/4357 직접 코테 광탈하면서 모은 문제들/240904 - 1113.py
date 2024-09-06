# 수영장 만들기
# 골드 1

n, m = map(int, input().split())

mat = [[] for _ in range(n)]

# bfs
# 일단 밖으로 나갈때까지 bfs 하고 그렇게 하기 위해 뚫어야 하는 최소 벽을 구하기..?