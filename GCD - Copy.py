def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Get input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Ensure the input is positive
num1 = abs(num1)
num2 = abs(num2)

# Calculate and display the GCD
gcd_result = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")
