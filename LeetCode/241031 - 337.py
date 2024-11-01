# House Robber III
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# tree에서의 recursive dp로 접근
# current node를 exclude, include 할 때 2가지 경우를 모두 return하는 것이 핵심

class Solution:
    def rob_subtree(self, node) -> (int, int):
        # retval: (exclude current, include current)
        # maximum of left subtree + max of right subtree / exclude current node

        if node is None:
            return (0, 0)
        exclude = 0

        left_sub = self.rob_subtree(node.left)
        right_sub = self.rob_subtree(node.right)
        exclude += max(left_sub)
        exclude += max(right_sub)

        include = left_sub[0] + right_sub[0] + node.val
        self.answer = max(exclude, include, self.answer)

        return (exclude, include)

    def rob(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        self.rob_subtree(root)
        return self.answer

        # 3 1 4 2 5