from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import CircularQueue
from linked_queue import LinkedQueue


def main():
    while True:
        print("\n=== STACK AND QUEUE MENU ===")
        print("1. Test Array Stack")
        print("2. Test Linked Stack")
        print("3. Test Circular Array Queue")
        print("4. Test Linked Queue")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            stack = ArrayStack()
            stack.push("A")
            stack.push("B")
            stack.display()
            stack.peek()
            stack.pop()
            stack.display()
        elif choice == "2":
            stack = LinkedStack()
            stack.push("A")
            stack.push("B")
            stack.display()
            stack.peek()
            stack.pop()
            stack.display()
        elif choice == "3":
            queue = CircularQueue()
            queue.enqueue("A")
            queue.enqueue("B")
            queue.display()
            queue.dequeue()
            queue.enqueue("C")
            queue.display()
        elif choice == "4":
            queue = LinkedQueue()
            queue.enqueue("A")
            queue.enqueue("B")
            queue.display()
            queue.dequeue()
            queue.display()
        elif choice == "5":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
