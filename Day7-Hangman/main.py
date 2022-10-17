import random
from hangman_words import word_list
from hangman_art import stages, logo


lifes = 6

print(logo)

chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)

# while there are blank spaces inside chosen word
while "_" in display:
    
    print(stages[lifes])
    print(f"{' '.join(display)}")

    if lifes == 0:
        break

    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("YOU HAVE ALREADY GUESSED THAT LETTER")

    if guess not in chosen_word:
        print("No match")
        lifes -= 1

    else:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = chosen_word[position]
if lifes != 0:
    print("YOU WIN!!")
else:
    print("You Lose")








