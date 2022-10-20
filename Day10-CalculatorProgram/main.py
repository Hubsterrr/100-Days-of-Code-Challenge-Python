# Functions with output
#
# def format_name(f_name, l_name):
#     title_name = f_name.title()
#     title_surname = l_name.title()
#     return f"{title_name} {title_surname}"
#
#
# print(format_name("HUBERT", "LUSZCZYSZYN"))
######## CODING EXERCISE - 10.1 ########

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     days = month_days[month - 1]
#     if is_leap(year) and month == 2:
#         days += 1
#     return days
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

######### DAY 10 PROJECT - CALCULATOR PROGRAM ########
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
