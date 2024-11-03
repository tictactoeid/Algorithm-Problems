# Serialize and Deserialize Binary Tree
# Hard

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize_helper(self, node):
        # do preorder traversal.
        if node is None:
            self.nodes.append("None")
            return

        self.nodes.append(str(node.val))
        self.serialize_helper(node.left)
        self.serialize_helper(node.right)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.nodes = []
        self.serialize_helper(root)
        return " ".join(self.nodes)

    def deserialize_helper(self):
        if self.idx >= self.n:
            return None

        if self.nodes[self.idx] == "None":
            self.idx += 1
            return None

        value = int(self.nodes[self.idx])
        node = TreeNode(value)
        self.idx += 1

        node.left = self.deserialize_helper()
        node.right = self.deserialize_helper()
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.idx = 0
        self.nodes = data.split()
        self.n = len(self.nodes)
        x = self.deserialize_helper()
        return x

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
