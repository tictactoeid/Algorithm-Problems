# Validate Binary Search Tree
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if node is None:
            return

        self.helper(node.left)
        self.answer.append(node.val)
        self.helper(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.answer = []
        self.helper(root)
        for i in range(0, len(self.answer) - 1):
            if self.answer[i] >= self.answer[i + 1]:
                return False
        return True
