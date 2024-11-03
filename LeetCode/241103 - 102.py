# Binary Tree Level Order Traversal
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, node, level):
        if node is None:
            return

        if level < len(self.level_order):
            self.level_order[level].append(node.val)
        else:
            self.level_order.append([node.val])

        self.postorder(node.left, level + 1)
        self.postorder(node.right, level + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.max_level = 0
        self.level_order = []
        self.postorder(root, 0)

        return self.level_order

