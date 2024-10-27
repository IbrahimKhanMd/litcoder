def phone_to_letters(digits: str):
    # Mapping of digits to corresponding letters
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # If input is empty, return an empty list
    if not digits:
        return []

    # Function to perform backtracking
    def backtrack(index, current_combination):
        # If the current combination length is equal to digits length, add it to results
        if index == len(digits):
            combinations.append(''.join(current_combination))
            return
        
        # Get letters corresponding to the current digit, skip if no mapping (like '1')
        if digits[index] in digit_to_char:
            possible_letters = digit_to_char[digits[index]]
            for letter in possible_letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()  # Backtrack
        else:
            backtrack(index + 1, current_combination)  # Skip digits with no mapping
    
    # Initialize a list to store combinations
    combinations = []
    
    # Start the backtracking process from index 0
    backtrack(0, [])
    
    return combinations

# Input through console
if __name__ == "__main__":
    digits = input("Enter digits: ")
    result = phone_to_letters(digits)
    print(' '.join(result))