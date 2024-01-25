import random

class FibonacciChecker:
    def __init__(self):
        self.correct_answers = 0

    def calculate_fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calculate_fibonacci(n - 1) + self.calculate_fibonacci(n - 2)

    def run_program(self):
        for _ in range(5):
            nth_number = random.randint(1, 1001)

            # Calculate the Fibonacci sequence
            fibonacci_sequence = [self.calculate_fibonacci(i) for i in range(nth_number + 1)]

            # Prompt the user to enter the sequence
            user_sequence_str = input(f"Enter the {nth_number}th Fibonacci sequence (comma-separated): ")
            user_sequence = [int(num) for num in user_sequence_str.split(',')]

            # Compare the user's input with the calculated sequence
            if user_sequence == fibonacci_sequence:
                print("Great work! Your answer is correct.")
                self.correct_answers += 1
            else:
                print("Oops! Your answer is incorrect.")

        # Calculate and print the percentage of correct answers
        percentage_correct = (self.correct_answers / 5) * 100
        print(f"\nPercentage of correct answers: {percentage_correct:.2f}%")

        # Provide feedback based on the percentage
        if percentage_correct > 70:
            print("Excellent!")
        elif 60 <= percentage_correct <= 70:
            print("Very good.")
        elif 50 <= percentage_correct < 60:
            print("Good.")
        elif 40 <= percentage_correct < 50:
            print("Fair.")
        else:
            print("Fail.")

# Run the program
fibonacci_checker = FibonacciChecker()
fibonacci_checker.run_program()
