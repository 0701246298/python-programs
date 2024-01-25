def multiply_decimal_array(decimal_array, multiplier):
    whole_part = 0

    for i in range(len(decimal_array) - 1, -1, -1):
        product = decimal_array[i] * multiplier + whole_part
        decimal_array[i] = product % 10
        whole_part = product // 10

    return whole_part

# Example usage:
decimal_representation = [1, 4, 2, 8, 5, 7]  # Decimal representation of 1/7
multiplier = 3

whole_number_part = multiply_decimal_array(decimal_representation, multiplier)

print("Whole Number Part:", whole_number_part)
print("Updated Decimal Array:", decimal_representation)
