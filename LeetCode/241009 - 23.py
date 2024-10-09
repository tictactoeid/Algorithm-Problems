# Merge k Sorted Lists
# Hard

import heapq
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        current = None
        root = None
        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, idx, node = heapq.heappop(heap)  # idx: 몇 번째 list인지
            if current is None:
                current = node
                root = node
            else:
                current.next = node
                current = current.next

            if node.next is not None:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return root
