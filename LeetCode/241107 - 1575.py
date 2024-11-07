# Count All Possible Routes
# Hard

class Solution:
    def dp(self, city: int, fuel: int) -> int:
        # print(city, fuel)
        # retval: count of the all possible routes from current state to finish
        if fuel < 0:
            return 0
        elif fuel == 0:
            if city == self.finish:
                return 1
            return 0

        if (city, fuel) in self.memo:
            return self.memo[(city, fuel)]

        # idx = bisect.bisect_left(self.sorted_locations, (self.locations[city] - fuel, 0))

        count = 0

        for next_city in range(self.n):
            if next_city == city:
                continue
            next_fuel = fuel - abs(self.locations[next_city] - self.locations[city])
            count += self.dp(next_city, next_fuel)

        # for i in range(idx, self.n):
        #     location, next_city = self.sorted_locations[i]
        #     if city == next_city:
        #         continue
        #     if abs(location - city) > fuel:
        #         break
        #     count += self.dp(next_city, fuel - abs(location - city))
        if city == self.finish:
            count += 1

        count %= (10 ** 9 + 7)
        self.memo[(city, fuel)] = count
        return count

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.finish = finish
        self.locations = locations
        self.n = len(locations)
        self.sorted_locations = sorted([(location, i) for i, location in enumerate(locations)])
        self.memo = {}

        val = self.dp(start, fuel)
        # print(self.memo)
        return val

# 0 1 4 3 2
# 2 3 4 6 8

