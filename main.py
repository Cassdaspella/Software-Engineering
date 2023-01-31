### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources
###complete!###
    def check_resources(self, ingredients):
        for items in ingredients:
            if ingredients.get(items) <= self.machine_resources.get(items):
                return True
            else:
                print(f"There is not enough {items}! please pick another option")
                return False
        return True
        """if an if else statement: if - if the choice has less or equal to the resources return true to continue else - (sorry there is not enough ______)."""

        """Returns True when order can be made, False if ingredients are insufficient."""
###complete!###
    def process_coins(self):

        total = int(input("how many large dollars?: ")) * 1.00
        total += int(input("how many half dollars?: ")) * .5
        total += int(input("how many quarters?: ")) * .25
        total += int(input("how many nickels?: ")) * .05

        return total

        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
###complete!###
    def transaction_result(self, coins, cost):
        """do an if else statement:
            if - input coins (process_coins) are more or equal to the cost subtract and get the remainder for change
            else - do a print statement (sorry, that's not enough money. Money refunded.)"""
        if coins >= cost:
            coins -= cost
            """round the coins up"""
            print(coins)
            return True
        else:
            print("Sorry, that is not enough change. Money refunded")
            return False

        """Return True when the payment is accepted, or False if money is insufficient.
           """

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredients in order_ingredients:
            self.machine_resources.update({ingredients : self.machine_resources.get(ingredients) - order_ingredients.get(ingredients)})
###output complete###
###testing completed!###
### Make an instance of SandwichMachine class and write the rest of the codes###
class output:
    going_on = True
    sandwhichmaker = SandwichMachine(resources)
    while going_on:
        choice = input("small/medium/large/off/resources\n")
        if choice == "off":
            break
        elif choice == "resources":
            print(f"Bread:{resources['bread']} slice(s) "
                  f"Ham: {resources['ham']} slice(s) "
                  f"Cheese: {resources['cheese']} slice(s)")
        elif choice == "small" or choice == "medium" or choice == "large":
            if sandwhichmaker.check_resources(recipes.get(choice).get("ingredients")) == True:
                if sandwhichmaker.transaction_result(sandwhichmaker.process_coins(), recipes.get(choice).get("cost")) == True:
                    sandwhichmaker.make_sandwich(choice, recipes.get(choice).get("ingredients"))
                """get user input/choice here and check resources and process coins and then show transaction result/cost and make the sandwich"""
        else:
            print("Not an option. Please choose an option.")