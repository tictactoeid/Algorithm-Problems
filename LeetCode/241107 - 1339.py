# Maximum Product if Splitted Binary Tree
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, calc_product=False):
        if node is None:
            return 0

        current_sum = node.val + self.dfs(node.left, calc_product) + self.dfs(node.right, calc_product)

        if calc_product:
            self.answer = max(self.answer, (self.sum - current_sum) * current_sum)

        return current_sum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        self.sum = self.dfs(root, False)
        self.dfs(root, True)
        return self.answer % (10 ** 9 + 7)
