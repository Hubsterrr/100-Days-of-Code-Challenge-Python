programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Retrieving items from dictionary.
# print(programming_dictionary["Bug"])

# Adding new items to dictionary
# programming_dictionary["Loop"] = "The acton of doing something over and over again"


# Create empty dictionary
# empty_dictionary = {}

# Wipe existing dictionary
# programming_dictionary = {}

# Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)


# loop through dictionary

# for key in programming_dictionary:
#    print(programming_dictionary[key])

######## CODING EXERCISE - 9.1 ########

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
#
# student_grades = {}
#
# for student in student_scores:
#     if student_scores[student] >= 91:
#         student_grades[student] = "Outstanding"
#
#     elif student_scores[student] >= 81:
#         student_grades[student] = "Exceeds Expectations"
#
#     elif student_scores[student] >= 71:
#         student_grades[student] = "Acceptable"
#
#     else:
#         student_grades[student] = "Fail"
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

##################################################

# Nesting a list in a Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Frankfurt", "Stuttgart"]
# }

# Nesting dictionary inside dictionary
# cities = {
#     "cities_visited": ["Paris", "Lille", "Dijon"],
# }
#
#
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 10},
#     "Poland": {"cities_visited": ["Krakow", "Warsaw", "Gdansk", "Rzeszow"], "total_visits": 30},
# }

# Nesting dictionary in a list
#
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 10
#     },
#     {
#         "country": "Poland",
#         "cities_visited": ["Krakow", "Warsaw", "Gdansk", "Rzeszow"],
#         "total_visits": 30
#     },
# ]

######## CODING EXERCISE - 9.2 ########

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
#
# #to be added to the travel_log. 👇
#
# def add_new_country(user_country, user_visits, user_cities):
#   new_country = {
#     "country": user_country,
#     "visits": user_visits,
#     "cities": user_cities,
#   }
#   travel_log.append(new_country)
#
#
#
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


##################################################



######### DAY 9 PROJECT - BLIND AUCTION ########
from art import logo


# does almost the same as clear() function in replit
def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


# function which allows to create another bidder and store it as dictionary inside List called auction
def find_highest_bid():
    highest_bid = 0
    for bidder in auction:
        if auction[bidder] > highest_bid:
            winner_name = bidder
            highest_bid = auction[bidder]
    print(f'The winner is {winner_name} with a bid of £{highest_bid}')


# Variables
auction = {}
new_bid = "yes"

# Main Program
print(logo)
print("Welcome to the secret auction program")

while new_bid == "yes":
    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid?: £"))
    auction[user_name] = user_bid

    new_bid = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if new_bid == "yes":
        clear()
    else:
        clear()
        find_highest_bid()













