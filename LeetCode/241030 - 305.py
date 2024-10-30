# Number of Islands II
# Hard

class Solution:
    def find(self, r: int, c: int) -> (int, int):
        parent = self.parents[r][c]
        if parent == (r, c) or parent == (-1, -1):
            return r, c
        else:
            tmp = self.find(parent[0], parent[1])
            self.parents[r][c] = tmp
            return self.parents[r][c]

    def union(self, r1: int, c1: int, r2: int, c2: int) -> None:
        p1 = self.find(r1, c1)
        p2 = self.find(r2, c2)

        if p1 == p2:
            return

        self.parents[p1[0]][p1[1]] = p2

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # initalize -> O(mn)
        # loop -> O(k), k = len(positions)

        self.parents = [[(-1, -1) for j in range(n)] for i in range(m)]
        # -1, -1 indicates the water
        # water는 사실상 사용하지 않으므로 dict 같은 걸 활용하면 시간/공간 복잡도 모두 O(k)로 줄어들 듯
        self.m, self.n = m, n

        answer = [0 for _ in range(len(positions))]
        count = 0

        for i in range(len(positions)):
            r, c = positions[i]

            if self.parents[r][c] != (r, c):  # handle duplicated positions
                count += 1
                self.parents[r][c] = (r, c)
                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        if self.parents[x][y] == (-1, -1):
                            continue
                        # print(x, y, r, c, self.find(x, y), self.find(r, c))
                        if self.find(x, y) != self.find(r, c):
                            count -= 1
                            self.union(x, y, r, c)

            answer[i] = count

        return answer


