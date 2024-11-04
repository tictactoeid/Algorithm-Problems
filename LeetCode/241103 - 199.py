# Binary Tree Right Side View
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_helper(self, node, level):
        if node is None:
            return
        if level == len(self.rightmost):
            self.rightmost.append(node.val)

        self.dfs_helper(node.right, level + 1)
        self.dfs_helper(node.left, level + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rightmost = []
        self.dfs_helper(root, 0)
        return self.rightmost
