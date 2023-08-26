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

total_money = 0


def update_resources(require_resources):
    for res in require_resources:
        resources[res] -= require_resources[res]


def is_resources_available(require_resources):
    is_res_available = True
    for res in require_resources:
        if require_resources[res] > resources[res]:
            is_res_available = False
            print(f"Sorry there is not enough {res}.")
    return is_res_available


def is_enough_money(item_cost, user_money):
    is_enough = True
    if item_cost > user_money:
        print("Sorry that's not enough money. Money refunded.")
        is_enough = False
    else:
        change = round((user_money - item_cost), 2)
        # if change > 0:
        print(f"Here is ${change} dollars in change.")
    return is_enough


def insert_coin():
    user_total = 0
    print("Please insert coins.")
    user_total += int(input("how many quarters?: ")) * 0.25
    user_total += int(input("how many dimes?: ")) * 0.10
    user_total += int(input("how many nickles?: ")) * 0.05
    user_total += int(input("how many pennies?: ")) * 0.01
    return user_total


def make_coffee(user_input, require_resources):
    if is_resources_available(require_resources):
        user_total_money = insert_coin()
        item_cost = MENU[user_input]["cost"]
        if is_enough_money(item_cost, user_total_money):
            global total_money
            total_money += item_cost
            update_resources(require_resources)
            print(f"Here is your {user_input} ☕️. Enjoy!")


def user_commands(user_input):
    global total_money
    match user_input:
        case "off":
            exit()
        case "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${total_money}")

        case _:
            if not user_input in MENU:
                print("incorrect input try again")
                return

            require_resources = MENU[user_input]["ingredients"]
            make_coffee(user_input, require_resources)


def start_coffee_machine():
    user_coffe_choice = input("What would you like? (espresso/latte/cappuccino): ")
    user_commands(user_coffe_choice)
    start_coffee_machine()


start_coffee_machine()
