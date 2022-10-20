############### Blackjack Project #####################

import random
from art import logo
from time import sleep

# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Functions
def draw_starting_cards(player_cards):
    for _ in range(2):
        player_cards.append(random.choice(cards))


def sum_cards(player_cards):
    """sum player's cards values and check if it is not higher than 21.
    if it is, then look for Ace card and change its value into 1"""
    addition = sum(player_cards)
    if addition > 21:
        for index in range(0, len(player_cards)):
            if player_cards[index] == 11:
                player_cards[index] = 1
                break
    return sum(player_cards)


def get_another_card(player_cards):
    """add card to player's hand"""
    player_cards.append(random.choice(cards))


def blackjack():
    """BlackJack game - call that function to start the game"""
    user_cards = []
    computer_cards = []

    print(logo)

    # Shuffle
    random.shuffle(cards)
    print("Shuffling cards...")
    sleep(1)

    # Draw starting cards for user and computer
    draw_starting_cards(user_cards)
    draw_starting_cards(computer_cards)

    # sum user's cards and check if sum is not higher than 21
    # if bigger, change ace value from 11 into 1
    user_sum = sum_cards(user_cards)
    computer_sum = sum_cards(computer_cards)

    computer_first_card = computer_cards[0]
    print(f"    Your cards: {user_cards}, current score: {user_sum}")
    print(f"    computer's first card: {computer_first_card}")

    want_another_card = True
    while want_another_card:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "n":
            want_another_card = False
        else:
            get_another_card(user_cards)
            user_sum = sum_cards(user_cards)
            print(f"    Your cards: {user_cards}, current score: {user_sum}")
            print(f"    computer's first card: {computer_first_card}")
            if user_sum > 21:
                break

    while computer_sum < 17:
        get_another_card(computer_cards)
        computer_sum = sum_cards(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_sum}")
    print(f"    computer's final hand: {computer_cards}, final score: {computer_sum}")
    if user_sum > 21:
        print("You went over. You lose 😤")
    elif computer_sum > 21:
        print("Opponent went over. You win 😁")
    elif user_sum == computer_sum:
        print("Draw !!")
    elif user_sum == 21:
        print("BlackJack! You win!")
    elif computer_sum == 21:
        print("Computer has BlackJack! You lose")
    elif user_sum > computer_sum:
        print("You win!")
    else:
        print("Computer wins")

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        blackjack()


################ Main program starting point ###################

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()
