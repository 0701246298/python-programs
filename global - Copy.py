a = 0  # Initial value for variable 'a'
b = 0  # Initial value for variable 'b'

def calculate_average():
    global a, b  # Declare 'a' and 'b' as global

    # Update the values of 'a' and 'b'
    a = 5
    b = 7

    # Calculate the average
    average = (a + b) / 2

    return average

# Call the function to calculate the average and update the global variables
average_result = calculate_average()
print("Average:", average_result)

# Modify the global variables 'a' and 'b' from outside the function
a = 5
b = 5

# Call the function again to calculate the new average with modified values
average_result = calculate_average()
print("Updated Average:", average_result)
