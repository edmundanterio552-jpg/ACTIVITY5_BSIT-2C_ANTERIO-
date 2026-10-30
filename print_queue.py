from collections import deque


class PrintQueue:
    """A simple FIFO queue for print jobs."""

    def __init__(self):
        self.jobs = deque()

    def add_job(self, document):
        self.jobs.append(document)
        print(document, "added to print queue.")

    def print_next(self):
        if not self.jobs:
            print("No documents to print.")
            return None
        document = self.jobs.popleft()
        print("Printing:", document)
        return document

    def display(self):
        print("Waiting documents:", list(self.jobs))


if __name__ == "__main__":
    printer = PrintQueue()
    printer.add_job("Assignment.pdf")
    printer.add_job("Report.docx")
    printer.add_job("Project.txt")
    printer.display()
    printer.print_next()
    printer.display()
