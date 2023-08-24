MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2.5,
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

require_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

user_coins = {
    "quarters": 1,
    "dimes": 2,
    "nickel": 1,
    "pennies": 2
}

user_money = 2.5
total_money = 0

espresso_cost = MENU["espresso"]["cost"]
def is_resources_available(require_resources):
    is_res_available = True
    for res in resources:
        if require_resources[res]>resources[res]:
            is_res_available = False
            print(f"Sorry there is not enough {res}.")
    return is_res_available

def process_coin(user_coins):
    user_total = 0
    for coin in user_coins:
        if coin == "quarters":
            user_total += 0.25 * user_coins[coin]
        elif coin == "dimes":
            user_total += 0.10 * user_coins[coin]
        elif coin == "nickel":
            user_total += 0.05 * user_coins[coin]
        else:
            user_total += 0.01 * user_coins[coin]
    return user_total

def is_enough_money(item_cost,user_money):
    is_enough = True
    if item_cost > user_money:
        print("Sorry that's not enough money. Money refunded.")
        is_enough = False
    return is_enough

def user_commands(user_input):
    match user_input:
        case "off":
            exit()
        case "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${total_money}")
        case "check_availability":
            print(is_resources_available(require_resources))
        case "process_coin":
            if is_resources_available(require_resources):
                print(process_coin(user_coins))
        case "check_money":
            print(is_enough_money(espresso_cost,user_money))
            # return "I'm a teapot"

        # If an exact match is not confirmed, this last case will be used if provided
        # case _:
        #     return "Something's wrong with the internet"


def start_coffee_machine():
    # user_coffe_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # user_coffe_choice = "off"
    # user_coffe_choice = "report"
    # user_coffe_choice = "check_availability"
    # user_coffe_choice = "process_coin"
    print(espresso_cost)
    user_coffe_choice = "check_money"
    user_commands(user_coffe_choice)
    # start_coffee_machine()

start_coffee_machine()
