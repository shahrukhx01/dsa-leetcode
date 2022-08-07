class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            return

        if self.head is None:
            self.head = Node(data, None)

        if index == 0:
            self.head = Node(data, self.head)
            return

        cursor = self.head
        idx = 0
        while cursor:
            if idx == index - 1:
                cursor.next = Node(data, cursor.next)
            cursor = cursor.next
            idx += 1

    def insert_at_start(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        self.head = Node(data, self.head)
        return

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        cursor = self.head

        while cursor.next:
            cursor = cursor.next

        cursor.next = Node(data, None)

    def length(self):
        if self.head is None:
            print("Linked List is empty!!")
            return

        cursor = self.head
        size = 0

        while cursor:
            cursor = cursor.next
            size += 1

        return size

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            return

        if index == 0:
            self.head = self.head.next
            return

        cursor = self.head
        idx = 0

        while cursor:
            if idx == index - 1:
                cursor.next = cursor.next.next
            cursor = cursor.next
            idx += 1

    def print(self):
        if self.head is None:
            print("Linked List is empty!!")

        cursor = self.head

        nodes_data = ""
        while cursor:
            nodes_data += f" -> {cursor.data}"
            cursor = cursor.next

        print(nodes_data)


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_start(3)
    ll.insert_at_start(2)
    ll.insert_at_start(1)
    ll.print()

    print(ll.length())
    ll.remove_at(0)
    ll.print()

    ll.insert_at(0, 1)
    ll.print()

    ll.insert_at_end(4)
    ll.print()
