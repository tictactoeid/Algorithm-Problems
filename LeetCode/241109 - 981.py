# Time Based Key-Value Store
# Medium

class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # O(1)
        if key in self.dict:
            self.dict[key].append((timestamp, value))
        else:
            self.dict[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        # O(log k)

        if key not in self.dict or self.dict[key][0][0] > timestamp:
            return ""

        idx = bisect.bisect_right(self.dict[key], (timestamp, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"))  # FIXME
        idx -= 1
        return self.dict[key][idx][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
