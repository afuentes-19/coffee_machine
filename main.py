from coffee_specs import MENU
from coffee_specs import resources

def powerOff(switch):
    global coffee_machine
    if switch == "off":
        coffee_machine = "off"

def printReport(current_resources):
    print("************************")
    print("REPORT")
    for resource in current_resources:
        print(f"{resource}: {current_resources[resource]}")
    print("************************")
    input("Press Enter to Continue")

def showMenu():
    print("MENU:")
    for drink in MENU:
        print(f"> {drink.capitalize()}: ${MENU[drink]['cost']}")

def checkResources(drink):
    required_resources = MENU[drink]["ingredients"]
    machine_resources = resources
    isSufficient = True
    lackingResources = []
    for resource in required_resources:
        # TESTING
        # print(f"Looking at {resource}")
        # print("The machine has..")
        # print(machine_resources[resource])
        # print("We need...")
        # print(required_resources[resource])
        if machine_resources[resource] < required_resources[resource]:
            isSufficient = False
            lackingResources.append(resource)
    return {"enoughResources": isSufficient, "lackingResources": lackingResources}

def calculateUserCoins(quarters, dimes, nickels, pennies):
    return ((quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01))

def processPayment(drink):
    drink_cost = MENU[drink]['cost']
    print(f"You asked for a {drink}")
    print(f"Please enter ${drink_cost}")
    print("Coins only.")
    transactionSuccess = True
    quarters_amt = 0
    dimes_amt = 0
    nickels_amt = 0
    pennies_amt = 0
    try:
        quarters_amt = int(input("Press enter amount of quarters: "))
        dimes_amt = int(input("Please enter amount of dimes: "))
        nickels_amt = int(input("Please enter amount of nickels: "))
        pennies_amt = int(input("Please enter amount of pennies: "))
    except ValueError as e:
        print(f"Sorry, you must enter a number: {e}")
        input("Press ENTER to continue")
    total_amt = calculateUserCoins(quarters_amt, dimes_amt, nickels_amt, pennies_amt)
    if total_amt < drink_cost:
        print("Sorry, that is not enough. Money refunded.")
        transactionSuccess = False
    elif total_amt > drink_cost:
        print(f"Thank you! Here is your change: ${(total_amt-drink_cost)}")
    else:
        print(f"Thank you!")
    return transactionSuccess

def deductResources(drink):
    global machine_resources
    required_resources = MENU[drink]["ingredients"]
    for resource in required_resources:
        machine_resources[resource] -= required_resources[resource]

def processDrink(drink):
    # check if the drink is in the menu 
    if not drink in MENU:
        print("Sorry, this drink is not in the menu")
        input("Press ENTER to continue")
        return
    # check if there are enough resources 
    resource_results = checkResources(drink)
    if not resource_results["enoughResources"]:
        for resource in resource_results["lackingResources"]:
            print(f"Sorry, there is not enough {resource}")
            input("Press ENTER to continue")
            return 
    # process coins
    good_payment = processPayment(drink)
    if good_payment:
        deductResources(drink)
        print(f"Your drink is ready! Enjoy your {drink}")
        input("Press ENTER to continue")
    else:
        return False



# initialize variables
machine_resources = resources
coffee_machine = "on"

while coffee_machine == "on":
    # show the menu
    showMenu()
    # prompt the user by asking what would you like 
    userInput = input("What would you like to drink?\n")
    userInput = userInput.lower()
    # show report of resources
    if userInput == "report":
        printReport(machine_resources)
    elif userInput == "off":
        print("I love you booboo! Hope you enjoyed your coffee <3")
        powerOff(userInput)
    else:
        processDrink(userInput)
        
    