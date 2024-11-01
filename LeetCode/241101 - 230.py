# Kth Smallest Element in a BST
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.sorted.append(node.val)
        self.inorder(node.right)

    # O(n) for inorder traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sorted = []
        self.inorder(root)
        return self.sorted[k - 1]