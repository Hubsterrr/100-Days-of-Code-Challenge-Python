from game_data import data
from art import logo, vs, question
from random import randint


def get_index():
    """Prints data from dictionary. Returns follower count"""
    index = randint(0, (len(data) - 1))
    return index


def get_follower_count(index):
    """Returns follower count from dictionary under given index"""
    follower_count = data[index]["follower_count"]
    return follower_count


def comparison_string(index):
    """Prints data from dictionary. Returns follower count"""
    name = data[index]["name"]
    description = data[index]["description"]
    country = data[index]["country"]
    return f"{name}, {description}, {country}"


def check_answer(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"


def higher_or_lower():
    """Runs game 'Higher or lower'"""
    player_is_right = True
    score = 0
    while player_is_right:
        print(logo)
        print(question)
        if score == 0:
            value_a = get_index()
            print(f"Compare A: {comparison_string(value_a)}")
            follower_a = get_follower_count(value_a)
        else:
            print(f"You are right! Current Score {score}")
            value_a = value_b
            print(f"Compare A: {comparison_string(value_a)}")
            follower_a = get_follower_count(value_a)
        print(vs)
        value_b = get_index()
        while value_a == value_b:
            value_b = get_index()
        print(f"Against B: {comparison_string(value_b)}")
        follower_b = get_follower_count(value_b)
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess, follower_a, follower_b)
        if is_correct:
            print("POINT")
            score += 1
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            player_is_right = False


higher_or_lower()
