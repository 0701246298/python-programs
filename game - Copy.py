import random


class GuessingGame:
    def __init__(self):
        self.lives = 3
        self.level = 1
        self.correct_answers = 0

    def play_game(self):
        print(f"Level {self.level} - You have {self.lives} lives.")

        while self.lives > 0:
            # Generate a random number for the correct answer
            correct_answer = random.randint(1, 10)

            try:
                # Ask the player to make a guess
                guess = int(input("Guess the number (1-10): "))

                if guess == correct_answer:
                    print("Correct! You guessed the number.")
                    self.correct_answers += 1
                else:
                    print("Wrong guess. Try again.")
                    self.lives -= 1

                if self.correct_answers == 3:
                    print("Congratulations! You've advanced to the next level.")
                    self.level += 1
                    self.correct_answers = 0
                    self.lives = 3
                    break
            except ValueError:
                print("Please enter a valid number (1-10).")

        if self.lives == 0:
            print("You've run out of lives. Game over.")
            return False

        return True

    def start(self):
        games_played = 0

        while games_played < 5:
            if self.play_game():
                games_played += 1
            else:
                break

        print("You've reached the end of the game.")


if __name__ == "__main__":
    game = GuessingGame()
    game.start()
