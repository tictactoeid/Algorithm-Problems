# 동전 문제
# 골드 2

dp = [0 for _ in range(100)]

dp[0] = 0
dp[1] = 1
dp[10] = 1
dp[25] = 1
for i in range(1, 10):
    dp[i] = i

for i in range(11, 25):
    dp[i] = (i//10) + (i%10)

for i in range(26, 100):
    dp[i] = min(
        1 + dp[i-25],
        1 + dp[i-10]
    )


def coin(price):
    count = 0
    while price:
        count += dp[price % 100]
        price = price // 100
    return count


# def coin(price, count):
#     if price < 25:
#         return count + (price // 10) + (price % 10)
#
#     k1 = len(str(price)) - 1
#     k2 = (len(str(price // 25)) - 1) // 2
#     if k1 % 2 == 0:
#         # k1이 짝수인 경우
#         # 예를 들어, 10000 vs 2500인 경우 10000은 2500의 배수이므로 무조건 10000을 선택
#         max_coin = 10 ** k1
#         return coin(price % max_coin, price // max_coin + count)
#     else:
#         coin_1 = 10 ** k1
#         coin_2 = 25 * (100 ** k2)
#         #print(price, coin_1, coin_2)
#         return min(
#             coin(price % coin_1, price // coin_1 + count),
#             coin(price % coin_2, price // coin_2 + count)
#         )

#print(coin(30, 0))


t = int(input())
for _ in range(t):
    price = int(input())
    print(coin(price))
