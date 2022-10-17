#### Day 5 - for loop

#fruits = ["apple", "Peach", "Pear"]
#for fruit in fruits:
#    print(fruit)
#    print(fruit + " Pie")


#### Day 5 - for loop: range() function

#for number in range(1, 10):    # not including 10
#    print(number)

# every step + 3
#for number in range(1, 10, 3):
#    print(number)
#total = 0
#for number in range(1, 101):
#    total += number
#print(total)

########## DAY 5 PROJECT - RANDOM PASSWORD GENERATOR ##################

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
#
# amount_of_char = nr_numbers + nr_symbols + nr_letters
# password = []
#
# for n in range(0, nr_letters + 1):
#     letter = random.randint(0, len(letters))
#     print(letter)
#     password.append(letters[letter-1])
#
# for y in range(0, nr_numbers ):
#     number = random.randint(0, len(numbers))
#     print(number)
#     password.append(numbers[number-1])
#
# for z in range(0, nr_symbols + 1):
#     symbol_id = random.randint(0, len(symbols))
#     print(symbol_id)
#     password.append(symbols[symbol_id-1])
#
# random.shuffle(password)
# final_password = ""
# for x in range(0, amount_of_char):
#     final_password += password[x]
# print("Here is your final password: " + final_password)




########## DAY 5 PROJECT - RANDOM PASSWORD GENERATOR ################## 2nd VERSION

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


amount_of_char = nr_numbers + nr_symbols + nr_letters
password = []

for n in range(0, nr_letters):
    password += random.choice(letters)


for n in range(0, nr_numbers):
    password += random.choice(numbers)


for n in range(0, nr_symbols):
    password += random.choice(symbols)


random.shuffle(password)
final_password = ""
for x in password:
    final_password += x
print("Here is your final password: " + final_password)


