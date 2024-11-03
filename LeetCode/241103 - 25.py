# Reverse Nodes in k-Group
# Hard

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []

        dummy = ListNode(0)
        dummy.next = head

        before = dummy
        node = head

        while node is not None:
            stack.append(node)
            node = node.next

            if len(stack) == k:
                while stack:
                    tmp = stack.pop()
                    tmp.next = None  # ListNode 간 cycle error 처리
                    before.next = tmp
                    before = before.next

        if stack:
            before.next = stack[0]
        return dummy.next

