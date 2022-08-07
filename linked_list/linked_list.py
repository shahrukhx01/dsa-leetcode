class Node:
    """
    A node class representing a single node entity in an instance of linkedlist
    """

    def __init__(self, data, next):
        """
        Initializes a node instance

        Args:
            data : value to be stored in the node
            next : next node in the linked list
        """
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        """
        Inserts a node at the beginning of the linkedlist

        Args:
            data : value for the node to be inserted
        """

        if self.head is None:
            self.head = Node(data, None)
            return

        self.head = Node(data, self.head)
        return

    def insert_at_end(self, data):
        """
        Inserts an elements at the end of the linked list

        Args:
            data : content of the node being inserted at the end
        """
        if self.head is None:
            self.head = Node(data, None)
            return

        cursor = self.head

        while cursor.next:
            cursor = cursor.next

        cursor.next = Node(data, None)

    def length(self):
        length = 0
        cursor = self.head
        while cursor:
            length += 1
            cursor = cursor.next
        return length

    def insert_at(self, index, data):
        """
        Inserts an elements at a specific index.

        Args:
            index : index of the element to be inserted
            data : data to be inserted
        """
        if index < 0 or index >= self.length():
            print("invalid index")
            return

        if self.head is None:
            self.head = Node(data, None)
            return

        cursor = self.head
        idx = 0
        while cursor:
            if index - 1 == idx:
                cursor.next = Node(data, cursor.next)
                break
            cursor = cursor.next
            idx += 1

    def remove_at(self, index):
        """
        Removes an elements at a specific index.

        Args:
            index : index of the element to be deleted
        """
        if index < 0 or index >= self.length():
            print("invalid index")
            return

        if self.head is None:
            return

        cursor = self.head
        idx = 0
        while cursor:
            if index - 1 == idx:
                cursor.next = cursor.next.next
                break
            cursor = cursor.next
            idx += 1

    def print(self):
        if self.head is None:
            print("Linked List is empty!")

        cursor = self.head
        contents = ""

        while cursor:
            contents += f" -> {str(cursor.data)}"
            cursor = cursor.next

        print(contents)


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_start("blueberry")
    ll.insert_at_start("mango")
    ll.insert_at_start("grapes")
    ll.print()
    ll.insert_at_end("orange")
    ll.print()
    ll.insert_at(2, "banana")
    ll.print()

    # remove banana
    ll.remove_at(2)
    ll.print()

    # remove blueberry
    ll.remove_at(2)
    ll.print()
