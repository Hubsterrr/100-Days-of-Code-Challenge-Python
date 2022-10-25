# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepSkyBlue")
# timmy.forward(100.0)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
#
# table = PrettyTable()
# table.add_column("Pokemon name", ["Pikatchu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "r"
# print(table)


################# DAY 15 - OOP COFFEE MACHINE ###################
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()


is_running = True
while is_running:
    menu_options = menu.get_items()
    user_input = input(f"What would you like? ({menu_options}): ").lower()
    if user_input == "report":
        machine.report()
        money.report()
    elif user_input == "off":
        is_running = False
    else:
        drink = menu.find_drink(user_input)
        if drink is None:
            break
        if machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            machine.make_coffee(drink)


