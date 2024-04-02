# 알파벳
# 골드 4
from collections import deque
import sys
r, c = map(int, input().split())

matrix = ['' for _ in range(r)]

for i in range(r):
    matrix[i] = sys.stdin.readline().strip()

visited_alpha = [False for _ in range(26)]
depth_max = 1
node = (0, 0)
visited_alpha[ord(matrix[node[0]][node[1]]) - ord('A')] = True

def dfs(node, depth): # backtracking
    global depth_max, visited_alpha
    depth_max = max(depth_max, depth)
    neighbors = [(node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)]
    for neighbor in neighbors:
        if 0 <= neighbor[0] <= r-1 and 0 <= neighbor[1] <= c-1:
            neighbor_alpha = ord(matrix[neighbor[0]][neighbor[1]]) - 65
            if not visited_alpha[neighbor_alpha]:
                visited_alpha[neighbor_alpha] = True
                dfs(neighbor, depth+1)
                visited_alpha[neighbor_alpha] = False

dfs(node, 1)
print(depth_max)