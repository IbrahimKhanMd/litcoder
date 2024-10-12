class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    # Function to transfer elements from stack_in to stack_out
    def transfer(self):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

    # Enqueue operation
    def enqueue(self, x):
        self.stack_in.append(x)

    # Dequeue operation
    def dequeue(self):
        if not self.stack_out:
            self.transfer()
        if self.stack_out:
            self.stack_out.pop()

    # Print front operation
    def print_front(self):
        if not self.stack_out:
            self.transfer()
        if self.stack_out:
            print(self.stack_out[-1])

# Function to handle the input queries
def process_queries():
    queue = QueueUsingTwoStacks()

    queries = input().split(',')
    for query in queries:
        q = query.split()
        if q[0] == "1":  # Enqueue operation
            queue.enqueue(int(q[1]))
        elif q[0] == "2":  # Dequeue operation
            queue.dequeue()
        elif q[0] == "3":  # Print front operation
            queue.print_front()

# Start processing the input queries
process_queries()