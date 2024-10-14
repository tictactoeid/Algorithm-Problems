# Course Schedule
# Medium

from enum import Enum


class State(Enum):
    not_visited = 0
    visiting = 1
    visited = 2


class Solution:
    def dfs(self, node: int) -> bool:
        if self.state[node] == State.visiting:
            return False

        self.state[node] = State.visiting

        if node in self.edges:
            for next_node in self.edges[node]:
                if self.state[next_node] != State.visited:
                    if not self.dfs(next_node):
                        return False

        self.state[node] = State.visited
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.state = [State.not_visited for _ in range(numCourses)]
        self.edges = {}
        for a_i, b_i in prerequisites:
            if b_i in self.edges:
                self.edges[b_i].append(a_i)
            else:
                self.edges[b_i] = [a_i]

        for node in range(numCourses):
            if self.state[node] == State.not_visited:
                if not self.dfs(node):
                    return False
        return True

