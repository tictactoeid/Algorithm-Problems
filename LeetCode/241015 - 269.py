# Alien Dictionary
# Hard

# Topological sort
# words의 order가 invalid한 edge cases가 있었음

from collections import deque


class Solution:
    def addEdge(self, successor: str, predecessor: str) -> None:
        for idx, char in enumerate(successor):
            if idx > len(predecessor) - 1:
                # "abc, ab"와 같이, 순서가 뒤인 단어가 앞인 단어의 prefix인 경우
                # 이는 invalid한 input이다.
                return False
            if char == predecessor[idx]:
                continue
            if char in self.edges:
                self.edges[char].add(predecessor[idx])
            else:
                self.edges[char] = set(predecessor[idx])
            return True

        # 단순히 successor == predecessor인 경우이므로, valid한 input
        return True

    def alienOrder(self, words: List[str]) -> str:
        self.edges = {}
        letters = set()

        for word in words:
            for x in word:
                letters.add(x)

        for i in range(len(words) - 1):
            if not self.addEdge(words[i], words[i + 1]):
                return ""

        indegrees = {}

        for letter in letters:
            indegrees[letter] = 0

        for node_succ in self.edges:
            for node_pred in self.edges[node_succ]:
                indegrees[node_pred] += 1

        # print(indegrees)
        # print(letters)
        # print(self.edges)

        q = deque()
        for letter in letters:
            if not indegrees[letter]:
                q.append(letter)

        answer = ""
        while q:
            node = q.popleft()
            answer += node
            if node in self.edges:
                for next_node in self.edges[node]:
                    indegrees[next_node] -= 1
                    if not indegrees[next_node]:
                        q.append(next_node)

        if len(answer) != len(letters):
            return ""

        return answer