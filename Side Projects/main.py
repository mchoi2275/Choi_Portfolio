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


# TODO 1. Print report.
def ask_input():
    '''Customer input and also the off switch and report'''
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino) ")
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            report()
        else:
            drink = MENU[choice]
            if check_resources(drink['ingredients']):
                print(choice, ' $', drink['cost'])
                payment = process_coins()
                if transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink['ingredients'])


def report():
    '''Produces a report for the user to see'''
    print(f"Water {resources['water']} ml")
    print(f"Milk {resources['milk']} ml")
    print(f"Coffee {resources['coffee']} g")
    print(f"Money : ${profit}")


# TODO 2. Check resources sufficient?
def check_resources(ordered_ingredients):
    '''Checks if there is sufficient ingredients in the resource dictionary'''
    for item in ordered_ingredients:
        if ordered_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO 3. Process coins.
def process_coins():
    '''Processes the amount of coins the customer inputs'''
    print('Please enter coins')
    total = 0
    total += int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.10
    total += int(input('How many nickels?: ')) * 0.05
    return total


# TODO 4. Check transaction successful?
def transaction_successful(money_received, drink_cost):
    '''Checks if the customer has enough money and provides change'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print('Insufficient money, please try again.')
        return False


# TODO 5. Make Coffee.
def make_coffee(drink_name, order_ingredients):
    '''Makes the coffee and deducts the order ingredients from the resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


ask_input()