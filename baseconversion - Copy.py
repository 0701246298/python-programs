def convert_to_base_n_with_interval(decimal_array, base):
    lower_bound = decimal_array.copy()
    upper_bound = [digit + 1 for digit in decimal_array]

    result = []

    while lower_bound != upper_bound:
        # Calculate midpoint
        midpoint = [(lower + upper) // 2 for lower, upper in zip(lower_bound, upper_bound)]

        # Check if the midpoint is within the interval
        if is_within_interval(midpoint, lower_bound, upper_bound):
            result.append(midpoint[0])
            lower_bound = midpoint
        else:
            result.append(midpoint[0] - 1)
            upper_bound = midpoint

    return result


def is_within_interval(midpoint, lower_bound, upper_bound):
    # Check if the midpoint is within the interval [lower_bound, upper_bound)
    return all(l <= m < u for l, m, u in zip(lower_bound, midpoint, upper_bound))


# Example usage:
decimal_representation = [1, 4, 2, 8, 5, 7]  # Decimal representation of 1/7
base_n_representation = convert_to_base_n_with_interval(decimal_representation, 16)

print("Decimal Representation:", decimal_representation)
print("Base-N Representation:", base_n_representation)
