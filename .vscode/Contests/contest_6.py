class TimeTravelersArchive:
    def __init__(self):
        # Dictionary to store key-timestamp-value mappings
        self.archive = {}

    def Store(self, key, value, timestamp):
       
        if key not in self.archive:
            self.archive[key] = []
        
        # Each entry is a tuple of (timestamp, value)
        self.archive[key].append((timestamp, value))
        # Keep the list sorted by timestamp for O(log n) retrieval
        self.archive[key].sort(key=lambda x: x[0])

    def Retrieve(self, key, timestamp):
        if key not in self.archive:
            return "empty"

        entries = self.archive[key]
        
        # Binary search to find the latest entry less than or equal to timestamp
        left, right = 0, len(entries) - 1
        result_idx = -1

        while left <= right:
            mid = (left + right) // 2
            if entries[mid][0] <= timestamp:
                result_idx = mid
                left = mid + 1
            else:
                right = mid - 1

        if result_idx == -1:
            return "empty"
        return entries[result_idx][1]

    def __getattr__(self, name):
        def method(*args):
            return "Wrong method called, please call Store or Retrieve method"
        return method

def process_commands(commands):
    archive = TimeTravelersArchive()
    
    for command in commands:
        parts = command.split()
        method = parts[0]
        
        if method == "Store":
            key, value, timestamp = parts[1], parts[2], int(parts[3])
            archive.Store(key, value, timestamp)
        elif method == "Retrieve":
            key, timestamp = parts[1], int(parts[2])
            result = archive.Retrieve(key, timestamp)
            print(result)

# Test Case 1
test1 = [
    "Store key1 value1 1",
    "Store key1 value2 2",
    "Retrieve key1 1",
    "Retrieve key1 3",
    "Retrieve key1 0"
]
process_commands(test1)

print()  # Empty line between test cases

# Test Case 2
test2 = [
    "Store key1 value1 1",
    "Store key1 value2 2",
    "Store key2 value1 3",
    "Store key1 value3 4",
    "Store key2 value2 5",
    "Retrieve key1 1",
    "Retrieve key2 5",
    "Retrieve key1 10"
]
process_commands(test2)

print()  # Empty line between test cases

# Test Case 3
test3 = [
    "Store language Latin 10",
    "Store language Old_English 50",
    "Store language Middle_English 90",
    "Store language2 Middle_English 90",
    "Store language1 Latin 190",
    "Store language3 Latin 5",
    "Store language1 Middle_English 20",
    "Retrieve language 2",
    "Retrieve language1 200",
    "Retrieve language3 60",
    "Retrieve language 90"
]
process_commands(test3)