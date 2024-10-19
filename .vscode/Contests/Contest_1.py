from collections import Counter

def backtrack(counter):
    total_sequences = 0
    for char in counter:
        if counter[char] > 0:
            # Use this letter and recurse
            counter[char] -= 1
            total_sequences += 1 + backtrack(counter)
            # Backtrack by restoring the count
            counter[char] += 1
    return total_sequences

def num_tile_possibilities(tiles: str) -> int:
    counter = Counter(tiles)
    return backtrack(counter)

# Get the input from the user
tiles = input("Enter the letters on the tiles: ")

# Compute and print the number of distinct non-empty sequences
output = num_tile_possibilities(tiles)
print(output)