from asyncio import QueueFull
from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, data):
        self.container.appendleft(data)

    def dequeue(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":

    queue = Queue()

    queue.enqueue(19)
    queue.enqueue(20)
    queue.enqueue(13)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue.is_empty())
