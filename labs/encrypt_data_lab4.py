def encrypt(input_value):
    if not input_value.isdigit():
        return "Enter only integer value"
    number = int(input_value)
    if number < 1000:
        return "Provided input is less than 4, enter four digit integers"
    elif number > 9999:
        return "Provided input is more than 4, enter four digit integers"
    elif number < 0:
        return "Enter positive 4-digit integer"
    digits = [int(digit) for digit in input_value]
    encrypted_digits = [(digit + 5) % 10 for digit in digits]
    encrypted_digits[0], encrypted_digits[2] = encrypted_digits[2], encrypted_digits[0]
    encrypted_digits[1], encrypted_digits[3] = encrypted_digits[3], encrypted_digits[1]
    return ''.join(map(str, encrypted_digits))
user_input = input("Enter a 4-digit integer: ")
print(encrypt(user_input))