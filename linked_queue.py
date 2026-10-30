class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """A queue implemented using linked nodes."""

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        print(data, "added to queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow!")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print("Removed:", data)
        return data

    def display(self):
        current = self.front
        items = []
        while current:
            items.append(current.data)
            current = current.next
        print("Queue (front to rear):", items)


if __name__ == "__main__":
    queue = LinkedQueue()
    queue.enqueue("First")
    queue.enqueue("Second")
    queue.enqueue("Third")
    queue.display()
    queue.dequeue()
    queue.display()
