##################### Scope #####################
#
# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# # Local scope
#
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()

# Global constant
# PI = 3.14


################# DAY 12 PROJECT - NUMBER GUESSING GAME ###################
import random
from art import logo
from random import randint


def set_difficulty():
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_choice == "hard":
        return 5
    elif user_choice == "easy":
        return 10
    else:
        return print("INVALID INPUT")


def check_answer(lifes, user_input, random_nr):
    """Checks if guess is bigger or lower than random number (random_number)"""
    if user_input > random_nr:
        print("Too high.")
        lifes -= 1
    elif user_input < random_nr:
        print("Too low.")
        lifes -= 1
    return lifes


def nr_guess_game():
    """Runs the number guessing game"""
    guess = ""
    health = None
    random_number = int(randint(1, 100))
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while health is None:
        health = set_difficulty()

    while random_number != guess:
        print(f"You have {health} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        health = check_answer(health, guess, random_number)
        if health == 0:
            print("You have run out of guesses, you lose")
            break

    if random_number == guess:
        print(f"You got it! The answer was {random_number}")


question = input("Do you wan to play a game? Type 'y' or 'n': ")
if question == 'y':
    nr_guess_game()
