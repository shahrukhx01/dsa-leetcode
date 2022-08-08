from collections import deque


class Stack:
    def __init__(self):
        """
        Initializes an empty Stack.
        """
        self.container = deque()

    def push(self, val):
        """
        Inserts a value at the top of the Stack.

        Args:
            val : Value to be inserted.
        """
        self.container.append(val)

    def pop(self):
        """
        Removes and returns the top of the Stack value.
        """
        return self.container.pop()

    def peek(self):
        """
        Returns the top value of the Stack.
        """
        return self.container[-1]

    def print(self):
        """
        Prints out the contents of the Stack.
        """

        contents = ""

        for val in self.container:
            contents += f" {val} <- "
        contents += "(top)"
        print(contents)


if __name__ == "__main__":
    stack = Stack()

    stack.push(3)
    stack.print()
    stack.push(2)
    stack.print()
    stack.push(1)
    stack.print()

    print("Top of Stack: ", stack.peek())
    print("Removing top of Stack: ", stack.pop())
    print("Top of Stack: ", stack.peek())
    stack.print()
