# Course Schedule II
# Medium

from collections import deque


class Solution:
    def dfs(self, node: int, path: set) -> bool:
        if node in path:
            return False

        if self.visited[node]:
            return True

        self.visited[node] = True
        path.add(node)
        if node in self.edges:
            for next_node in self.edges[node]:
                # if not self.visited[next_node]:
                if not self.dfs(next_node, path):
                    return False
        path.remove(node)
        self.stack.append(node)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.edges = {}
        self.visited = [False for _ in range(numCourses)]
        self.stack = []

        for a, b in prerequisites:
            if b in self.edges:
                self.edges[b].append(a)
            else:
                self.edges[b] = [a]

        for i in range(numCourses):
            if not self.visited[i]:
                if not self.dfs(i, set()):
                    return []  # cycle detected

        return self.stack[::-1]

    def findOrder_indeg(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {}

        indegrees = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            if b in edges:
                edges[b].append(a)
            else:
                edges[b] = [a]
            indegrees[a] += 1

        q = deque()

        for i in range(numCourses):
            if not indegrees[i]:
                q.append(i)

        answer = []

        while q:
            node = q.popleft()
            answer.append(node)
            if node in edges:
                for dst in edges[node]:
                    indegrees[dst] -= 1
                    if not indegrees[dst]:
                        q.append(dst)

        if len(answer) != numCourses:
            return []
        return answer

