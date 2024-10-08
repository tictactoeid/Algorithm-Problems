# Add Two Numbers
# Medium

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # self.answer = []
    def addDigit(self, n1: Optional[ListNode], n2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if n1 is None and n2 is None:
            if carry:
                # self.answer.append(ListNode(carry, None))
                return ListNode(carry, None)
            else:
                return None

        elif n1 is None:
            value = n2.val + carry
            next = n2.next
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0
            # self.answer.append(ListNode(value, addDigit(None, next, carry)))
            return ListNode(value, self.addDigit(None, next, carry))

        elif n2 is None:
            value = n1.val + carry
            next = n1.next
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0
            # self.answer.append(ListNode(value, addDigit(next, None, carry)))
            return ListNode(value, self.addDigit(next, None, carry))

        else:
            value = n1.val + n2.val + carry
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0
            # self.answer.append(ListNode())
            return ListNode(value, self.addDigit(n1.next, n2.next, carry))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        tmp = self.addDigit(l1, l2, 0)
        return tmp
        # while tmp is not None:
        #     answer.append(tmp)
        #     print(tmp.val)
        #     tmp = tmp.next
        # return answer
