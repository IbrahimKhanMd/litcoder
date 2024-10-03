def cumulative_sum(num):
    return sum(int(digit) for digit in str(num)) if num >= 10 else num

def alphabetize_odd_numbers(num):
    return ''.join(chr(ord('a') + (int(digit) - 1)) if int(digit) % 2 else digit for digit in str(num))

def solve():
    input_str = inpt()
    numbers = [cumulative_sum(int(num)) for num in input_str.split()]
    return ''.join(alphabetize_odd_numbers(num) for num in numbers)

print(solve()) 

#
def get_single_digit_sum(num):
    # Keep summing digits until we get a single digit
    while num > 9:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        num = sum_digits
    return num

def number_to_alphabet(num):
    # Convert numbers to alphabets (1=a, 2=b, etc.)
    # Only convert odd numbers, keep even numbers as is
    if num % 2 == 1:
        return chr(ord('a') + num - 1)
    return str(num)

def generate_pin(numbers):
    pin = ""
    # Process each number in the array
    for num in numbers:
        # Get single digit sum
        single_digit = get_single_digit_sum(num)
        # Convert to alphabet if odd, keep as number if even
        pin += number_to_alphabet(single_digit)
    return pin

def main():
    try:
        # Get input from user
        print("Enter the numbers separated by spaces:")
        numbers = list(map(int, input().strip().split()))
        
        # Generate and display PIN
        pin = generate_pin(numbers)
        print(f"Generated PIN: {pin}")
        
    except ValueError:
        print("Please enter valid numbers separated by spaces")
    except Exception as e:
        print(f"An error occurred: {e}")

if _name_ == "_main_":
    main()