# Word Break II
# Hard

class Node:
    def __init__(self, char: str, word=None):
        self.char = char
        self.word = None
        self.children = {}  # char: Node


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert_word(self, word: str):
        node = self.root
        for x in word:
            if x in node.children:
                node = node.children[x]
            else:
                node.children[x] = Node(x)
                node = node.children[x]

        node.word = word

    def has_word(self, word: str) -> bool:
        node = self.root
        for x in word:
            if x not in node.children:
                return False
            node = node.children[x]

        return node.word == word


class Solution:
    def dfs(self, s: str, indices: List[str] = [0]):
        start_idx = indices[-1]
        # print(indices)
        if start_idx == len(s):
            output = ""
            for i in range(len(indices) - 1):
                output += s[indices[i]:indices[i + 1]]
                output += " "
            self.answer.append(output.rstrip())
            return
        for idx in range(start_idx + 1, len(s) + 1):
            if self.trie.has_word(s[start_idx:idx]):
                self.dfs(s, indices + [idx])

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.trie = Trie()
        self.answer = []
        for word in wordDict:
            self.trie.insert_word(word)

        self.dfs(s, [0])
        return self.answer
