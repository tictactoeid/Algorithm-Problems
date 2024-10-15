# Word Ladder
# Hard

# BFS
# wordList를 이중 loop하며 O(n^2)로 edge를 채우면 TLE
# 대신 각 word의 길이가 최대 10밖에 안 되므로,
# 각 word를 한 글자씩 바꿔가며 wordList에 있다면 neighbor에 추가

from collections import deque


class Solution:
    def getNeighbors(self, word: str) -> List[str]:
        neighbors = []

        for i in range(len(word)):
            for j in range(26):
                char = chr(ord('a') + j)
                if char == word[i]:
                    continue
                new_word = word[:i] + char + word[i + 1:]
                if new_word in self.wordSet:
                    neighbors.append(new_word)
                # neighbors.append(word[:i] + char + word[i+1:])

        return neighbors

    # def isNeighbor(self, src: str, dst: str) -> bool:
    #     count = 0
    #     for i in range(len(src)):
    #         if src[i] != dst[i]:
    #             count += 1
    #             if count > 1:
    #                 break

    #     return count == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.wordSet = set(wordList)
        if endWord not in self.wordSet:
            return 0
        # edges = {}

        # edges[beginWord] = []

        # for word in wordList:
        #     if self.isNeighbor(beginWord, word):
        #         edges[beginWord].append(word)

        # for i, word in enumerate(wordList):
        #     if word == beginWord:
        #         continue
        #     if word not in edges:
        #         edges[word] = set()
        #     for j in range(len(wordList)):
        #         if self.isNeighbor(word, wordList[j]):
        #             edges[word].add(wordList[j])

        # print(edges)

        q = deque()
        q.append((1, beginWord))

        visited = set()
        visited.add(beginWord)

        while q:
            distance, node = q.popleft()
            if node == endWord:
                return distance

            for neighbor in self.getNeighbors(node):
                if neighbor not in visited:
                    if neighbor == endWord:
                        return distance + 1
                    q.append((distance + 1, neighbor))
                    visited.add(neighbor)

        return 0
