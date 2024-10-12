# Word Search II
# Hard

# Trie의 delete 연산 구현
# Trie + backtracking

class Node:
    def __init__(self, char: str, word: str = None):
        self.char = char
        self.word = None
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert_word(self, word: str) -> None:
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
            if x in node.children:
                node = node.children[x]
            else:
                return False

        return node.word == word

    def has_prefix(self, prefix: str) -> bool:
        node = self.root
        for x in prefix:
            if x in node.children:
                node = node.children[x]
            else:
                return False

        return True

    def remove_word(self, word: str):
        node = self.root
        stack = []
        for x in word:
            stack.append((node, x))
            node = node.children[x]

        node.word = None
        if node.children:
            return

        while stack:
            node, x = stack.pop()
            if node.children[x].word is not None:
                return
            del node.children[x]
            if node.children:
                return


class Solution:
    def dfs(self, path: List[Tuple[int]], prefix: str):
        # TODO
        i, j = path[-1]
        if self.trie.has_word(prefix):
            self.answer.append(prefix)
            self.trie.remove_word(prefix)

        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for x, y in neighbors:
            if not (0 <= x < self.m and 0 <= y < self.n):
                continue
            if (x, y) not in path:
                next_prefix = prefix + self.board[x][y]
                if self.trie.has_prefix(next_prefix):
                    self.dfs(path + [(x, y)], next_prefix)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.answer = []

        for word in words:
            self.trie.insert_word(word)

        for i in range(self.m):
            for j in range(self.n):
                if self.trie.has_prefix(board[i][j]):
                    self.dfs([(i, j)], board[i][j])

        return self.answer
