# 리모컨
# 골드 5


# 그리디 아님...
n = int(input())
m = int(input())


if m != 0:
    broken_buttons = set(map(int, input().split()))
else:
    broken_buttons = set()

a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
buttons = a.difference(broken_buttons)



#
#
# def greedy_check_digit(value):
#     global broken_buttons
#     digit = int(value)
#     left_candidate = None
#     right_candidate = None
#
#     for i in range(digit, -1, -1):
#         if i not in broken_buttons:
#             left_candidate = i
#             break
#
#     for i in range(digit, 10, 1):
#         if i not in broken_buttons:
#             right_candidate = i
#             break
#
#     return left_candidate, right_candidate
#
#
# def greedy_candidate(prefer_small = True):
#     candidate = ""
#     for digit in str(n):
#         left, right = greedy_check_digit(digit)
#
#         if left is None:
#             candidate += str(right)
#             break
#         elif right is None:
#             candidate += str(left)
#             break
#
#         if str(left) == digit and str(right) == digit:
#             candidate += str(digit)
#         else:
#             if (int(digit) - left) < (right - int(digit)):
#                 candidate += str(left)
#                 break
#             elif (int(digit) - left) > (right - int(digit)):
#                 candidate += str(right)
#                 break
#             elif prefer_small:
#                 candidate += str(left)
#                 break
#             else:
#                 candidate += str(right)
#                 break
#
#     if len(candidate) == len(str(n)):
#         return int(candidate)
#
#     if int(candidate) < int(str(n)[:len(candidate)]):
#         # get largest button
#         for i in range(9, -1, -1):
#             if i not in broken_buttons:
#                 candidate += str(i) * (len(str(n)) - len(candidate))
#     else:
#         # get smallest button
#         for i in range(0, 10, 1):
#             if i not in broken_buttons:
#                 candidate += str(i) * (len(str(n)) - len(candidate))
#     return int(candidate)
#
#
# if m < 10:
#     small_candidate = greedy_candidate(True)
#     big_candidate = greedy_candidate(False)
#
#     small_btn_count = len(str(small_candidate)) + abs(n - small_candidate)
#     big_btn_count = len(str(big_candidate)) + abs(n - big_candidate)
#     curr_btn_count = abs(100 - n)
#
#     print(min(small_btn_count, big_btn_count, curr_btn_count))
#     print(small_candidate, big_candidate)
#
# else:
#     print(abs(100-n))
#
