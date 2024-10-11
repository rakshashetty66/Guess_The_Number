import random
import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return None


def check_answer(guessed_number, answer):
    if guessed_number < answer:
        print("Your guess is too low.")
        return False
    elif guessed_number > answer:
        print("Your guess is too high.")
        return False
    else:
        print(f"Your guess is right! The answer was {answer}.")
        return True


def game():
    print(logo.logo)
    print("Let me think of a number between 1 to 50.")
    answer = random.randint(1, 50)

    level = input("Choose level of difficulty... Type 'easy' or 'hard': ")
    attempts = set_difficulty(level)

    if attempts is None:
        print("You have entered an invalid difficulty level... Play Again!")
        return

    guessed_number = 0  # Initialize guessed_number

    while attempts > 0 and guessed_number != answer:
        print(f"You have {attempts} remaining to guess the number.")

        try:
            guessed_number = int(input("Guess a number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Check if the guess is correct
        if check_answer(guessed_number, answer):
            break

        attempts -= 1

        if attempts == 0:
            print("You are out of guesses... You lose! The correct answer was:", answer)


game()
