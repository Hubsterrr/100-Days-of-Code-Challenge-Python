# def greet():
#     print("Hi")
#     print("how are you")
#     print("good to see you")
# greet()

# Function that allow for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#
# greet_with_name("Hubert")

# def greet_with(name, location):
#     print(f"Hi {name} you are in {location}")
# greet_with(name="Hubert", location="London")

######### DAY 8 PROJECT - CAESAR CIPHER ########
from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alphabet_shift = alphabet + alphabet
answer = "yes"


def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter not in alphabet_shift:
            end_text += letter
        else:
            letter_index = alphabet_shift.index(letter)
            end_text += alphabet_shift[letter_index + shift]
    print(f"The {direction}d text is {end_text}")


print(logo)
while answer == "yes":
    user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_text = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))
    if user_shift > 26:
        user_shift = user_shift % 26
    caesar(text=user_text, shift=user_shift, direction=user_direction)
    answer = input("Type 'yes' if you want to go again. otherwise type 'no'.\n").lower()
print("Goodbye!")
