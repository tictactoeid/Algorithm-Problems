# 리모컨
# 골드 5


# 그리디 아님...
import sys
from itertools import product

n = int(input())
m = int(input())

if m != 0:
    broken_buttons = set(map(int, input().split()))
else:
    print(min(abs(n-100), len(str(n))))
    sys.exit()

if m == 10:
    print(abs(n-100))
    sys.exit()

length = len(str(n))
buttons = []
for i in range(0, 10):
    if i not in broken_buttons:
        buttons.append(i)

if n == 0:
    if len(buttons) > 0:
        print(min(buttons)+1)

        sys.exit()

candidates = (list(product(buttons, repeat=length))
              + list(product(buttons, repeat=length + 1)))
if length > 1:
    candidates += (product(buttons, repeat=length - 1))
def tuple2int(x):
    result = 0
    for i in range(len(x)):
        result += x[i] * 10 ** (len(x) - i - 1)
    return result

result = min(candidates, key=lambda x: abs(tuple2int(x)-n) + len(str(tuple2int(x))))
value = tuple2int(result)
print(min(abs(value-n) + len(str(value)), abs(100-n)))
