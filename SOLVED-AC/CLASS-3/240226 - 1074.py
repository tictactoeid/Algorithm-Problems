# Z
# 실버 1

N, R, C = map(int, input().split())


# Z 순서대로 4등분하여, 각각 0 1 2 3사분면
def z(r, c, size, start):
    # size * size
    half = size // 2
    start_add_value = half ** 2

    if size == 1:
        return start

    if r < half: # 0, 1
        if c < half: # 0사분면
            return z(r, c, half, start)
        else: # 1사분면
            return z(r, c - half, half, start + start_add_value)
    else:
        if c < half: # 2사분면
            return z(r - half, c, half, start + start_add_value * 2)
        else: # 3사분면
            return z(r - half, c - half, half, start + start_add_value * 3)


print(z(R, C, 2**N, 0))