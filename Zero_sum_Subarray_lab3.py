def zero_sum_subarray(arr):
    # Check if the size of the array is valid
    n = len(arr)
    if n < 1 or n > 10:
        print("Array size must be between 1 and 10")
        return
    
    # Initialize variables
    sum_set = set()  # Set to store prefix sums
    current_sum = 0  # Prefix sum

    # Traverse through the array
    for num in arr:
        current_sum += num
        
        # If prefix sum becomes 0 or it has been seen before
        if current_sum == 0 or current_sum in sum_set:
            print("True")
            print(n)
            return
        
        # Add the current sum to the set
        sum_set.add(current_sum)
    
    # If no subarray with zero sum is found
    print("False")
    print(n)

# Input the array as space-separated integers
arr = list(map(int, input().split()))

# Call the function to check for a zero-sum subarray
zero_sum_subarray(arr)
