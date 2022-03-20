from coffee_data import MENU, resources

def format_report():
    water_remaining = resources["water"]
    milk_remaining = resources["milk"]
    coffee_remaining = resources["coffee"]
    money = 0.0
    return f"""Water: {water_remaining}
    Milk: {milk_remaining}
    Coffee: {coffee_remaining}
    Money: ${money}"""
   
# Function check to see if resources are sufficient

def check_resources(order):
    for ingredient in MENU[order]["ingredients"]:
        # res_status[ingredient] = 
        if MENU[order]["ingredients"][ingredient] <= resources[ingredient]: 
            pass #print(f"There's enough {ingredient}")
        else:
            print(f"There's not enough {ingredient}")
            quit()

## Function to make coffee 

def make_coffee(order):
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
        # print(f"{ingredient}: {MENU[order]['ingredients'][ingredient]}")
    print(f"Here's your {order}")
    return resources

# Function to get coins from

def accept_coins(order):
    cost = '{:.2f}'.format(round(MENU[order]["cost"], 2)) 
    print(f"A {order} costs {cost}")
    inserted_Q = int(input("Insert quarters: "))
    inserted_D = int(input("Insert dimes: "))
    inserted_N = int(input("Insert nickles: "))
    inserted_P = int(input("Insert pennies: "))    
    return inserted_Q*.25 + inserted_D*.10 + inserted_N*.05 + inserted_P*.01

# Functio to process transaction 
    
def check_transaction(payment, order):
    if payment >= MENU[order]["cost"]:
        resources["money"] += payment 
        #subtract resources
        if payment > MENU[order]["cost"]:
            change = payment - MENU[order]["cost"] 
            change = '{:.2f}'.format(round(change, 2))
            print(f"Here's ${change} in change")
        # print(f"Here's your {order}")
    else: 
        print("Not enough money")
        quit()
    
# Check the user's input to decide what to do next

def what_to_do():
    if order in MENU:
        check_resources(order)
        payment = accept_coins(order)
        check_transaction(payment, order)
        resources = make_coffee(order)
        # print(f"Here's your {order}")
    elif order == "off":
        quit()
    elif order == "report":
        report = format_report()
        print(report)
    else:
        print("Don't understand.")    


machine_on = True 
while machine_on:
    print(resources)
    order = input("What would you like? (espresso/latte/cappuccino): ")
    what_to_do()


