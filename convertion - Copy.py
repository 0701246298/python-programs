def convert_to_hexadecimal(decimal_array):
    hexadecimal_array = []

    # Perform the conversion for each digit in the array
    for digit in decimal_array:
        quotient = digit // 16
        remainder = digit % 16

        # Convert the quotient and remainder to hexadecimal digits
        hexadecimal_digit_quotient = str(quotient) if quotient < 10 else chr(ord('A') + quotient - 10)
        hexadecimal_digit_remainder = str(remainder) if remainder < 10 else chr(ord('A') + remainder - 10)

        # Append the hexadecimal digits to the result array
        hexadecimal_array.append(hexadecimal_digit_quotient)
        hexadecimal_array.append(hexadecimal_digit_remainder)

    # Remove leading zeros in the hexadecimal array
    while hexadecimal_array[0] == '0':
        hexadecimal_array.pop(0)

    return hexadecimal_array

# Example usage:
decimal_representation = [1, 4, 2, 8, 5, 7]  # Decimal representation of 1/7
hexadecimal_representation = convert_to_hexadecimal(decimal_representation)

print("Decimal Representation:", decimal_representation)
print("Hexadecimal Representation:", hexadecimal_representation)
