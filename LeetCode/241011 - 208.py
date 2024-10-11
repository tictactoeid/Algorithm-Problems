# Implement Trie
# Medium

class Node:
    def __init__(self, key: str, data=None):
        self.key = key  # a, p, p, l, e
        self.data = data  # apple
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node(key=None, data=None)

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        # 마지막
        node.data = word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            if node.data == word:
                return True

        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)