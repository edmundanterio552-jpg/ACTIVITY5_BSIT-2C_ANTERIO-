class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    """A stack implemented using linked nodes."""

    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        print(data, "added to stack.")

    def pop(self):
        if self.top is None:
            print("Stack Underflow!")
            return None
        data = self.top.data
        self.top = self.top.next
        print("Removed:", data)
        return data

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        print("Top item:", self.top.data)
        return self.top.data

    def display(self):
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next
        print("Stack (top to bottom):", items)


if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    stack.pop()
    stack.display()
