# N과 M (12)
# 실버 2

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

printed = set()
def dfs(i, arr):
    #visited.add(i)
    if len(arr) == m:
        out = ""
        for k in arr:
            out += str(nums[k])
            out += " "
        out.rstrip()
        if out not in printed:
            print(out)
            printed.add(out)
        return

    last = -1
    for j in range(i, n):
        if last == j:
            continue
        last = j
        dfs(j, arr + [j])

dfs(0, [])