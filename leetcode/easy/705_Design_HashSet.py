class MyHashSet:
    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if key in self.set:
            for idx, val in enumerate(self.set):
                if key == val:
                    del self.set[idx]
                    break

    def contains(self, key: int) -> bool:
        return key in self.set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
