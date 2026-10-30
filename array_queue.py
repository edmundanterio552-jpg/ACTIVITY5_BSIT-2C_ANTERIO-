class CircularQueue:
    """A circular queue implemented with a fixed-size list."""

    def __init__(self, capacity=3):
        self.items = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            print("Queue Overflow!")
            return
        rear = (self.front + self.size) % self.capacity
        self.items[rear] = item
        self.size += 1
        print(item, "added to queue.")

    def dequeue(self):
        if self.size == 0:
            print("Queue Underflow!")
            return None
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print("Removed:", item)
        return item

    def display(self):
        result = [
            self.items[(self.front + index) % self.capacity]
            for index in range(self.size)
        ]
        print("Queue (front to rear):", result)


if __name__ == "__main__":
    queue = CircularQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.display()
    queue.dequeue()
    queue.enqueue("D")
    queue.display()
