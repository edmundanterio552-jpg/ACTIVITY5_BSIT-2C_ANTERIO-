class ArrayStack:
    """A stack implemented with a list and a fixed capacity."""

    def __init__(self, capacity=3):
        self.items = []
        self.capacity = capacity

    def push(self, item):
        if len(self.items) >= self.capacity:
            print("Stack Overflow!")
            return
        self.items.append(item)
        print(item, "added to stack.")

    def pop(self):
        if not self.items:
            print("Stack Underflow!")
            return None
        item = self.items.pop()
        print("Removed:", item)
        return item

    def peek(self):
        if not self.items:
            print("Stack is empty.")
            return None
        print("Top item:", self.items[-1])
        return self.items[-1]

    def display(self):
        print("Stack:", self.items)


if __name__ == "__main__":
    stack = ArrayStack()
    stack.push("Apple")
    stack.push("Banana")
    stack.push("Orange")
    stack.display()
    stack.peek()
    stack.pop()
    stack.display()
