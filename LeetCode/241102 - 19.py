# Remove Nth Node From End of List
# Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd_stack(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first approach with stack
        # TC O(n), SC O(n)
        stack = []

        node = head
        while node is not None:
            stack.append(node)
            node = node.next

        target = stack[-n]
        target_next = target.next
        target_before = stack[-n - 1] if len(stack) >= n + 1 else None

        if len(stack) >= n + 1:
            target_before = stack[-n - 1]
            target_next = stack[-n].next
            target_before.next = target_next
            return head
        else:
            # target is the head.
            return head.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # follow up: do this in one pass
        # TC O(n), SC O(1)

        # track (n+1)th node every iteration
        parent = None
        count = 0

        node = head

        while node is not None:
            if count == n + 1:
                parent = parent.next
            else:
                count += 1
                if count == n + 1:
                    parent = head
            node = node.next

        if parent is not None:
            parent.next = parent.next.next  # if parent.next is not None else None
            return head
        else:
            # target is the head.
            return head.next
