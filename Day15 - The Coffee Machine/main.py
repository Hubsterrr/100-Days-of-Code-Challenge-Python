from data import MENU, resources


def get_resources():
    """Prints out resources from dictionary"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\n"
          f"Milk: {milk}ml\n"
          f"Coffee: {coffee}g")


def check_resources(coffee_type):
    """Returns missing insufficient resource based on coffee type. If there is nothing insufficient, nothing is
    returned """
    water_needed = MENU[coffee_type]["ingredients"]["water"]
    if coffee_type != "espresso":
        milk_needed = MENU[coffee_type]["ingredients"]["milk"]
        milk = resources["milk"]
        if milk_needed > milk:
            return "milk"
    coffee_needed = MENU[coffee_type]["ingredients"]["coffee"]
    water = resources["water"]
    coffee = resources["coffee"]
    if water_needed > water:
        return "water"
    elif coffee_needed > coffee:
        return "coffee"


def make_coffee(coffee_type):
    """Deducts resources from dictionary based on beverage needs"""
    if coffee_type != "espresso":
        milk_needed = MENU[coffee_type]["ingredients"]["milk"]
        resources["milk"] -= milk_needed
    water_needed = MENU[coffee_type]["ingredients"]["water"]
    resources["water"] -= water_needed
    coffee_needed = MENU[coffee_type]["ingredients"]["coffee"]
    resources["coffee"] -= coffee_needed


def insert_coins():
    """Returns total value of inserted coins"""
    print("Please insert coins.")
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.1
    total += float(input("How many nickles?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    return round(total, 2)


def get_cost(coffee_type):
    """Returns coffee price. As parameter function takes coffee name which appears in dictionary"""
    value = MENU[coffee_type]["cost"]
    return value


# Variables
is_running = True
money_in_machine = 0

while is_running:
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "report":
            get_resources()
            print(f"Money: {money_in_machine}$")
        elif order == "off":
            is_running = False
            break
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            price = get_cost(order)
            if check_resources(order) == "milk" or check_resources(order) == "water" or check_resources(order) == "coffee":
                print(f"Sorry there is not enough {check_resources(order)}.")
                is_running = False
                break
            money_inserted = insert_coins()
            if money_inserted < price:
                print("Sorry that's not enough money. Money Refunded")
                break
            change = round(money_inserted - price, 2)
            print(f"Here is ${change} in change")
            print(f"Here is your {order} ☕️. Enjoy!")
            make_coffee(order)
            money_in_machine += price
        else:
            print("INVALID INPUT!")




