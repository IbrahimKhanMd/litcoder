cipher = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}

def encrypt_decrypt(word, key, operation):
    if not isinstance(key, int):
        print("Enter valid key")
        return
    if operation not in ['addition', 'subtraction']:
        print("Invalid Operation")
        return
    if not word.isupper():
        print("Word should be in capitals")
        return
    
    result = ''
    
    for char in word:
        if char in cipher:
            new_char = cipher[char]
            ascii_value = ord(new_char)
            
            if operation == 'addition':
                new_ascii = ascii_value + key
            elif operation == 'subtraction':
                new_ascii = ascii_value - key
            
            result += chr(new_ascii)
    
    print(result)

# Taking input
key = int(input())
operation = input()
word = input()

# Calling the function
encrypt_decrypt(word, key, operation)