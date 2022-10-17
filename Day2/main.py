# Day 2 - Data types

# String = "hello" + [1]-informs which letter take out
# print("hello"[1])


# Day 2 - len()=integer - how to change integer to string

# num_char = len(input("what is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")


# Day 2 - operations in python

# 3 + 5
# 20 - 5
# 3 * 5
# 3 / 2 - changes to float
# 2 ** 3 - to the power of


# Day 2 - number manipulation and F strings in python

# round number by n decimals
# round(8 / 3, n))
# print(round(8/3,2))

# floor division //
# print(8 // 3)

# score = 0
# height = 1.8
# isWinning = True
#print(f"your score is {score}, your height {height}, {isWinning}")


#################### DAY 2 PROJECT - TIP CALCULATOR ########################

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?")) / 100
group_Size = float(input("How many people to split the bill?"))

to_Pay = (bill / group_Size) * (tip + 1)
print(f"Each person should pay: ${round(to_Pay, 2)}")




