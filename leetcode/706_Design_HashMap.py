class MyHashMap:
    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        for idx, item in enumerate(self.map):
            if key == item[0]:
                self.map[idx] = [key, value]
                return

        self.map.append([key, value])

    def get(self, key: int) -> int:
        val = -1
        for item in self.map:
            if key == item[0]:
                val = item[1]
                break
        return val

    def remove(self, key: int) -> None:
        for idx, item in enumerate(self.map):
            if key == item[0]:
                del self.map[idx]
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
