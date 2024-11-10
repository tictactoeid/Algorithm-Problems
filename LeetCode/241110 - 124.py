# Binary Tree Maximum Path Sum
# Hard

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node is None:
            return 0

        left_gain = max(0, self.dfs(node.left))
        right_gain = max(0, self.dfs(node.right))

        self.answer = max(self.answer, left_gain + node.val, right_gain + node.val, left_gain + right_gain + node.val)

        return max(left_gain, right_gain) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = -math.inf
        self.dfs(root)
        return self.answer
