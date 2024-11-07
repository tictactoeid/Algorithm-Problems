# Bus Routes
# Hard

class Solution:
    # def dp(self, stop):
    #     if stop == self.target:
    #         return 0

    #     if stop in self.memo:
    #         return self.memo[stop]

    #     value = math.inf
    #     for bus in self.buses[stop]:
    #         for next_stop in self.routes[bus]:
    #             if next_stop == stop:
    #                 continue
    #             value = min(value, self.dp(next_stop))

    #     return value

    def dp(self, bus, visited):
        # print(bus)
        visited[bus] = True

        if bus >= len(self.routes):
            return math.inf

        if bus in self.memo:
            return self.memo[bus]

        stops = self.routes[bus]

        if self.target in stops:
            self.memo[bus] = 1
            return 1

        value = math.inf
        for stop in stops:
            for next_bus in self.buses[stop]:
                if bus == next_bus:
                    continue
                if not visited[next_bus]:
                    visited[next_bus] = True
                    value = min(value, 1 + self.dp(next_bus, visited))
                    visited[next_bus] = False

        self.memo[bus] = value
        return self.memo[bus]

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        self.target = target
        self.routes = routes
        self.memo = {}

        self.buses = {}  # buses[i]: 정거장 i에 도착하는 버스
        self.visited = set()

        for bus, route in enumerate(routes):
            for stop in route:
                if stop in self.buses:
                    self.buses[stop].add(bus)
                else:
                    self.buses[stop] = set()
                    self.buses[stop].add(bus)

        # print(self.buses)

        answer = math.inf
        # print(self.buses[source])

        if source not in self.buses:
            return -1

        for bus in self.buses[source]:
            answer = min(answer, self.dp(bus, [False] * len(routes)))

        # print(self.memo)
        if answer == math.inf:
            return -1
        return answer


