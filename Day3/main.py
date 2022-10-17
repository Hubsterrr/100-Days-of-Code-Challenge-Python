# Day 3 - if / else conditional operators

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm?"))
#if height >= 120:
#    print("You can ride rollercoaster")
#else:
#    print("Sorry, you have to grow before you can ride.")


# Day 3 - nested if statement and elif statements, multiple if statements

# height = int(input("What is your height in cm?"))
# bill = 0
# if height >= 120:
#    print("You can ride rollercoaster")
#    age = int(input("What is your age?"))
#    if age < 12:
#       print("ticket is 5$")
#        bill = 5
#    elif age <= 18:
#        print("ticket is 7$")
#        bill = 7
#    else:
#        print("ticket is 12$")
#        bill = 12
#
#    wants_photo = input("Dou you want a photo? Y or N. ")
#    if wants_photo == "y" or "Y":
#        print("Additional 3$ will be added to your bill")
#        bill += 3

#    print(f"Your bill is {bill}")
#
# else:
#    print("Sorry, you have to grow before you can ride.")


################## DAY 3 PROJECT - TREASURE ISLAND ######################

print("Welcome to treasure island. Your mission is to find the treasure.")

first_choice = input("Left or Right?\n")
win = True
if (first_choice == "Left") or (first_choice == "left"):
    print("Go inside")
else:
    win = False
    print("You died.")

if win == True:
    second_choice = input("Swim or Wait?\n")
    if (second_choice == "Wait") or (second_choice == "wait"):
        print("Go Inside")
    else:
        win = False
        print("You died.")

if win == True:
    third_choice = input("Which door? blue, red, yellow")
    if (third_choice == "Yellow") or (third_choice == "yellow"):
        print("You WIN!")
    elif (third_choice == "Blue") or (third_choice == "blue"):
        win = False
        print("You diedddd")
    else:
        print("You died.")





