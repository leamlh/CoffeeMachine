MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_ressources_ok(choice):
    """ Check if there is enough of each ingredients. Returns True if yes, False if no """
    if resources["water"] <= MENU[choice]["ingredients"]["water"]:
        print("Sorry, there is not enought water")
        return False
    elif resources["coffee"] <= MENU[choice]["ingredients"]["coffee"]:
        print("Sorry, there is not enought coffee")
        return False
    elif choice != "espresso":
        if resources["milk"] <= MENU[choice]["ingredients"]["milk"]:
            print("Sorry, there is not enought milk")
            return False
        else:
            return True
    else:
        return True


def print_report():
    """ Print the amount of water, milk and coffee available"""
    print("Water: " + str(resources["water"]))
    print("Milk: " + str(resources["milk"]))
    print("Coffee: " + str(resources["coffee"]))
    print("Money: " + str(resources["money"]))


def process_coins(quarters, dimes, nickles, pennies):
    """ Calculates the total amount inserted """
    total_inserted = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_inserted


def check_transaction_ok(choice, quarters, dimes, nickles, pennies):
    if process_coins(quarters, dimes, nickles, pennies) < int(MENU[choice]["cost"]):
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif process_coins(quarters, dimes, nickles, pennies) > float(MENU[choice]["cost"]):
        change = process_coins(quarters, dimes, nickles, pennies) - float(MENU[choice]["cost"])
        change = round(change, 2)
        print(f"Here is ${change} dollars in change.")
        resources["money"] += float(MENU[choice]["cost"])
        return True
    else:
        resources["money"] += float(MENU[choice]["cost"])
        return True


def make_coffee(choice):
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    if choice != "espresso":
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    print(F"Here's your {choice}. Enjoy !")


client_choice = input("What would you like? (espresso/latte/cappuccino): ")

while client_choice != "off":
    if client_choice != "report":
        if check_ressources_ok(client_choice):
            print("Please insert coins")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            pennie = int(input("How many pennies?: "))
            if check_transaction_ok(client_choice, quarter, dime, nickle, pennie):
                make_coffee(client_choice)
    else:
        print_report()
    client_choice = input("What would you like? (espresso/latte/cappuccino): ")
