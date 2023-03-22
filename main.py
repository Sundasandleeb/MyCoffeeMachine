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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):

    for items in order_ingredients:

        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}, cant make your drink")
            return False
    return True


def process_coins():
    """Returns the total amount from coins inserted"""
    print("Enter coins")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))

    total_amount = float(0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies)
    return total_amount


def is_transaction_successful(money_received, drink_cost):

    if money_received < drink_cost:
        print("Sorry there is not enough money. Money refunded")
        return False
    else:
        remaining = round(money_received - drink_cost, 2)
        print(f"Here is ${remaining} in change")
        global profit
        profit += drink_cost
        return True


def make_coffee(drink_selected , ingredients):

    for items in ingredients:

        resources[items] -= ingredients[items]
    print(f"Here is your coffee ☕ , Enjoy !")


is_operating = True

while is_operating:

    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "off":
        is_operating = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment , drink["cost"]):
                make_coffee(user_choice , drink["ingredients"])























