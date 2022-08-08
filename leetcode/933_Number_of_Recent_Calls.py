from collections import deque


class RecentCounter:
    def __init__(self):
        self.recent_calls = deque()

    def ping(self, t: int) -> int:
        self.recent_calls.appendleft(t)

        calls = 0

        for time in self.recent_calls:
            if time >= t - 3000 and time <= t:
                calls += 1
            else:
                break

        return calls


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
