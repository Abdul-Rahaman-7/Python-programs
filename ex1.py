def reverse_digits(number):
    # Convert the number to a string
    num_str = str(number)
    # Reverse the string and convert it back to an integer
    reversed_num_str = num_str[::-1]
    reversed_number = int(reversed_num_str)
    return reversed_number

# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter an integer to reverse its digits: "))
        reversed_number = reverse_digits(number)
        print(f"Reversed number: {reversed_number}")
    except ValueError:
        print("Please enter a valid integer.")
