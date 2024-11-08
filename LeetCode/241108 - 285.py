# Inorder Successor in BST
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, node):
        # Approach 1

        if node is None:
            return

        if self.answer is not None:
            return

        self.inorder(node.left)

        self.before = self.current
        self.current = node
        if self.before == self.target:
            self.answer = node
            return

        self.inorder(node.right)

    def inorderSuccessor_1(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # Approach 1: inorder traversal
        # TC: O(N)
        # SC: O(N) (recursion stack)
        self.answer = None
        self.before = None
        self.current = None
        self.target = p

        self.inorder(root)

        return self.answer

    def inorderSuccessor(self, root, p):
        # Approach 2: use BST properties
        # TC: O(N), SC: O(1)

        # BST에서의 inorder successor -> sort했을 때 바로 다음 node

        node = root
        successor = None

        while node:
            if node.val <= p.val:
                node = node.right
            else:
                successor = node
                node = node.left

        return successor
