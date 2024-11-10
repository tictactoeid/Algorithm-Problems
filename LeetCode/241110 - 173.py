# Binary Search Tree Iterator
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator_1:
    # Approach 1: inorder traversal
    # TC: O(n) for init, O(1) for next and hasnext
    # SC: O(n)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.sorted.append(node.val)
        self.inorder(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.sorted = []
        self.inorder(root)

        self.idx = 0

    def next(self) -> int:
        value = self.sorted[self.idx]
        self.idx += 1
        return value

    def hasNext(self) -> bool:
        if self.idx >= len(self.sorted):
            return False
        return True


class BSTIterator:
    # Approach 2: stack + BST properties (follow-up)
    # TC: O(1) for avg case
    # SC: O(h)

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while node is not None:
            self.stack.append(node)
            node = node.left

        # [7, 3]
        # [7]
        # [7, 15, 9]
        # [7, 15]
        # [7, 15, 20]

    def next(self) -> int:
        current = self.stack.pop()

        if current.right is not None:
            node = current.right
            while node is not None:
                self.stack.append(node)
                node = node.left
        return current.val

    def hasNext(self) -> bool:
        return bool(self.stack)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()