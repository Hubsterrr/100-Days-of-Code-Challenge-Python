# Day 4 - Randomisation

# import random

# random_integer = random.randint(0, 4)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)


# Day 4 - list

#united_states = ["Delaware", "Pennsylvania", "Utah"]

# united_states[0] - delaware
# united_states[-1] - Utah (last item from the list)

#united_states.append("HubertLand")

#print(united_states)


# Day 4 - nested list

#fruits = ["strawberries", "Apples", "Grapes"]
#vegetables = ["Kale", "Tomatoes", "Celery", "Potatoes"]

#dirty_dozen = [fruits, vegetables]

#print(dirty_dozen[1][0])



############ DAY 4 PROJECT - ROCK,PAPER,SCISORS###########

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random


player_move = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors."))
computer_move = random.randint(0, 2)

print("\nplayer move: ")
if player_move == 0:
    print(rock)
elif player_move == 1:
    print(paper)
elif player_move == 2:
    print(scissors)

print("computer move: ")
if computer_move == 0:
    print(rock)
elif computer_move == 1:
    print(paper)
elif player_move == 2:
    print(scissors)

if player_move < 0 or player_move > 2:
    print("you have put wrong number. you loose.")
else:
    if player_move == computer_move:
        print("DRAW!")
    elif (player_move == 0) and (computer_move == 2):
        print("PLAYER WINS")
    elif (player_move == 2) and (computer_move == 1):
        print("PLAYER WINS")
    elif (player_move == 1) and (computer_move == 0):
        print("PLAYER WINS")

    elif (computer_move == 0) and (player_move == 2):
        print("COMPUTER WINS")
    elif (computer_move == 2) and (player_move == 1):
        print("COMPUTER WINS")
    elif (computer_move == 1) and (player_move == 0):
        print("COMPUTER WINS")

















