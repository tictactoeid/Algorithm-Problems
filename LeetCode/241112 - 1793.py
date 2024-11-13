# Maximum Score of a Good Subarray
# Hard
# Moloco 기출

from typing import *

def update_score(low, high, minimum_element, maximum_score) -> int:
    length = high - low - 1
    return max(maximum_score, length * minimum_element)


def extend_low(arr, low, high, minimum_element, maximum_score):
    minimum_element = min(minimum_element, arr[low])
    low -= 1
    maximum_score = update_score(low, high, minimum_element, maximum_score)
    return low, maximum_score, minimum_element


def extend_high(arr, low, high, minimum_element, maximum_score):
    minimum_element = min(minimum_element, arr[high])
    high += 1
    maximum_score = update_score(low, high, minimum_element, maximum_score)
    return high, maximum_score, minimum_element


def get_maximum_score(arr: List[int], k: int) -> int:
    # 시간 복잡도: O(n)
    # 공간 복잡도: O(1)
    low = k - 1
    high = k + 1

    minimum_element = arr[k]
    maximum_score = arr[k] * 1

    while low >= 0 or high < len(arr):  # TC: O(n)
        # arr[low] vs min

        # left_element = arr[low] if low >= 0 else -math.inf
        # extend if (next element) >= (minimum)
        if low >= 0 and arr[low] >= minimum_element:
            low, maximum_score, minimum_element = extend_low(arr, low, high, minimum_element, maximum_score)
        elif high < len(arr) and arr[high] >= minimum_element:
            high, maximum_score, minimum_element = extend_high(arr, low, high, minimum_element, maximum_score)

        # otherwise, take larger one
        else:
            if low >= 0 and high < len(arr):
                if arr[low] >= arr[high]:
                    low, maximum_score, minimum_element = extend_low(arr, low, high, minimum_element, maximum_score)
                else:  # arr[low] < arr[high]
                    high, maximum_score, minimum_element = extend_high(arr, low, high, minimum_element, maximum_score)
            # reached border
            elif low == -1:
                high, maximum_score, minimum_element = extend_high(arr, low, high, minimum_element, maximum_score)
            else:  # high == len(arr)
                low, maximum_score, minimum_element = extend_low(arr, low, high, minimum_element, maximum_score)

    return maximum_score
