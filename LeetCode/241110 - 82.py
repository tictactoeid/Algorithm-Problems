# Remove Duplicates from Sorted List II
# Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        target = None

        dummy = ListNode()  # dummy node
        dummy.next = head

        before = dummy
        node = head

        while node:
            if target == node.val:
                before.next = node.next
            else:
                if node.next is not None and node.next.val == node.val:
                    target = node.val
                    before.next = node.next
                else:
                    target = None
                    before = node
            node = node.next

        return dummy.next
