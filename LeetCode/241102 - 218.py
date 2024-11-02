# The Skyline Problem
# Hard

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # x좌표를 순회하며, 현재 x좌표에 해당하는 가장 높은 천장이 갱신될 때마다 answer에 추가해 줌
        # 가장 높은 천장을 track하기 위해 maxheap을 사용
        # TLE 발생하여, x를 +1씩 iterate하지 않고 buildings에 나오는 좌표값들만 확인하도록 수정
        # 또한 heap이 빈 경우 바닥을 answer에 추가해줘야 함에 유의

        x_coordinates = set()
        for building in buildings:
            x_coordinates.add(building[0])
            x_coordinates.add(building[1])

        x_coordinates = sorted(list(x_coordinates))

        idx = 0
        answer = []

        heap = []
        heapq.heappush(heap, (
            -buildings[0][2],
            buildings[0][1]
        ))
        idx += 1

        for x in x_coordinates:
            while heap and heap[0][1] <= x:
                # out of scope
                heapq.heappop(heap)

            while idx < len(buildings) and buildings[idx][0] <= x:  # 여러 빌딩의 왼쪽 좌표가 겹칠 수 있으므로 if가 아닌 while임에 유의
                heapq.heappush(heap, (
                    -buildings[idx][2],  # height, max heap
                    buildings[idx][1]  # end x-coordinate
                ))
                idx += 1

            if heap:
                # print(x, heap)
                if not answer or answer[-1][1] != -heap[0][0]:  # check duplicates
                    answer.append([x, -heap[0][0]])
            else:  # floor
                if not answer or answer[-1][1] != 0:  # check duplicates
                    answer.append([x, 0])

            x += 1

        return answer


