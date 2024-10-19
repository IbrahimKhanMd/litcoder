def can_transform(start, end):
    # If the count of 'L' and 'R' characters doesn't match, return False
    if start.replace('X', '') != end.replace('X', ''):
        return False

    # Two pointers to compare 'L' and 'R' positions in start and end strings
    i, j = 0, 0
    n = len(start)

    while i < n and j < n:
        # Skip 'X' characters in both strings
        while i < n and start[i] == 'X':
            i += 1
        while j < n and end[j] == 'X':
            j += 1

        # If either pointer goes out of bounds, break the loop
        if i == n or j == n:
            break

        # If characters don't match, return False
        if start[i] != end[j]:
            return False

        # 'L' can only move to the left (i >= j), 'R' can only move to the right (i <= j)
        if (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
            return False

        i += 1
        j += 1

    # Both strings should have been completely traversed, ignoring 'X's
    # Also need to ensure that after skipping 'X's, both pointers have reached the end
    while i < n and start[i] == 'X':
        i += 1
    while j < n and end[j] == 'X':
        j += 1

    return i == n and j == n

# Function to handle input and output
def process_input():
    start = input().strip()
    end = input().strip()
    result = can_transform(start, end)
    print(result)

# Example usage
process_input()