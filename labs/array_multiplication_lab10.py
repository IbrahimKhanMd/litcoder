def arrayManipulation(n, queries):
   
    arr = [0] * (n + 1)
    for query in queries:
        start, end, value = query
        arr[start - 1] += value  # Start index is inclusive, so add value
        if end <= n:
            arr[end] -= value  # End+1 index (exclusive), so subtract value
    max_value = 0
    current_value = 0
    for i in range(n):
        current_value += arr[i]
        if current_value > max_value:
            max_value = current_value
    return max_value
# Input handling
if __name__ == "__main__":
    # First input: size of the array
    n = int(input()) 
    # Second input: number of queries
    q = int(input())  
    # Next q lines: each containing 3 integers representing a query
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    # Call the function and print the result
    result = arrayManipulation(n, queries)
    print(result)