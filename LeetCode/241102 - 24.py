# Swap Nodes in Pairs
# Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode()
        dummy.next = head

        parent = dummy
        first = head
        second = head.next

        while parent is not None and parent.next is not None and parent.next.next is not None:
            first.next = second.next
            second.next = first
            parent.next = second

            parent = first
            first = parent.next
            if parent.next is None:
                break
            second = parent.next.next

        return dummy.next

        # parent -> first -> second -> next
        # parent -> second -> first -> next
