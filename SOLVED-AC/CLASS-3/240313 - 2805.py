# 나무 자르기
# 실버 2

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = 1000000000

# start <= height <= end
while start <= end:
    if end <= start == 1:
        break

    height = (start + end) // 2

    tree_sum = 0
    for tree in trees:
        tree_sum += max(0, tree - height)
    #print(start, end, height, tree_sum)

    if tree_sum < m:
        end = height
    elif tree_sum == m:
        break
    else:
        start = height

print(height)