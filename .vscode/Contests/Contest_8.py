def bit_matching(A):
    # Function to count matching bits in binary representation
    def f(X, Y):
        return bin(~(X ^ Y) & 0b111).count('1')
    
    # Check for invalid input
    if any(num < 0 or num >= 8 for num in A):
        return "Invalid Input"
    
    # Calculate sum of matching bits for all ordered pairs
    N = len(A)
    result = 0
    for i in range(N):
        for j in range(N):
            result += f(A[i], A[j])
    
    return result

# Taking input from user
A = list(map(int, input().split()))
print(bit_matching(A))