# LCS
# 골드 5

str1 = input()
str2 = input()

n = len(str1)
m = len(str2)

mat = [[0 for _ in range(m+1)] for _ in range(n+1)]


for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            continue # mat[i][j] = 0
        if str1[i-1] == str2[j-1]:
            mat[i][j] = mat[i-1][j-1] + 1
        else:
            mat[i][j] = max(mat[i-1][j], mat[i][j-1])


print(mat[n][m]) # length