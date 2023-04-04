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
}
profit = 0


def sufficient_resources(drink):
    """Takes a desired drink, and returns True if there are sufficient resources to make a drink, False otherwise."""
    for item in drink['ingredients']:
        if drink['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins(drink):
    """Takes a desired drink and returns the total cost on making it."""
    quarters = int(input("How many quarters would you insert? "))
    dimes = int(input("How many dimes would you insert? "))
    nickles = int(input("How many nickles would you insert? "))
    pennies = int(input("How many pennies would you insert? "))
    return quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01


def deplete_recourses_and_profit(drink):
    """Takes drink and reduces amounts of resources used to make the drink from the bank."""
    global profit
    profit += drink['cost']
    for item in drink['ingredients']:
        resources[item] -= drink['ingredients'][item]


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
        print("The machine is turned off for maintenance break.\n")
    elif choice == "report":
        print(f"""
        Water: {resources['water']}ml
        Milk: {resources['milk']}ml
        Coffee: {resources['coffee']}g
        Money: ${profit}
""")
    elif choice in ['cappuccino', 'espresso', 'latte']:
        drink = MENU[choice]
        if sufficient_resources(drink):
            received = process_coins(drink)
            if received >= drink['cost']:
                deplete_recourses_and_profit(drink)
                print(f"Here is ${round(received-drink['cost'],2)} dollars in change.")
                print(f"Here is your {choice}. Enjoy!")
            else:
                print(f"Sorry that's not enough money. Money refunded.")
    else:
        print("Wrong Input, make sure you type the options correctly.")


