def count_divisible_pairs(arr, k):
    n = len(arr)
    count = 0
    pairs = []
    
    # Check all possible pairs
    for i in range(n):
        for j in range(i + 1, n):
            # If sum of pair is divisible by k, increment count and store pair
            if (arr[i] + arr[j]) % k == 0:
                count += 1
               # pairs.append((arr[i], arr[j]))
    
    # Print all valid pairs for verification
    
    return count

# Get input from user
k = int(input())  # Get the divisor

# Get the array input and convert it to integers
arr = list(map(int, input().split()))

# Calculate and print the result
result = count_divisible_pairs(arr, k)
print(result)