# Binary Tree Maximum Path Sum
# Hard

# bottom-up dp라는 아이디어 자체는 떠올렸으나
# tree에서의 재귀적 dp 구현에 어려움을 겪음
# 특히 구하려는 maximum과 재귀함수의 retval이 달라서

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtree_path(self, node):
        if node is None:
            return 0

        left = max(0, self.subtree_path(node.left))
        right = max(0, self.subtree_path(node.right))

        left_path = left + node.val
        right_path = right + node.val
        max_path = max(left_path, right_path)
        self.answer = max(left + right + node.val, self.answer)  # 현재 node를 root로 하는 path.
        return max_path  # left + right + val이 아닌 이유: 재귀적으로 path를 구해야 하므로 좌우 중 한 쪽만 갈 수 있음

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = -math.inf
        self.subtree_path(root)
        return self.answer