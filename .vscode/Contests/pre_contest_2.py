def bit_matching_count(A):
    max_bits = 3  # Since the problem restricts to 3-bit binary numbers (from 000 to 111)
    N = len(A)
    total_sum = 0

    # Iterate over all bit positions (0, 1, 2 for 3-bit numbers)
    for bit in range(max_bits):
        count_1 = 0
        count_0 = 0
        
        # Count how many numbers have a 1 or 0 at the current bit position
        for num in A:
            if num & (1 << bit):  # Check if the 'bit' position is set to 1
                count_1 += 1
            else:
                count_0 += 1
        
        # The number of matching bits for the current bit position
        total_sum += count_1 * count_1 + count_0 * count_0

    return total_sum

# Input the array of numbers from the user without prompt
A = list(map(int, input().split()))

# Calculate and print the result
output = bit_matching_count(A)
print(output)