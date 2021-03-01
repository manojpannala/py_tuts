from art import logo
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You go it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempt remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You are out of guesses, you lost.")
            return
        elif guess != answer:
            print("Guess again.")


game()
