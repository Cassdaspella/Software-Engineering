### Data ###
import data
from sandwich_maker import sandwich_maker
from cashier import cashier


### Complete functions ###

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker(data.resources)
cashier_instance = cashier()
###complete!###
def main():
    going_on = True
    while going_on:
        choice = input("What would you like? small/medium/large/off/resources\n")
        if choice == "off":
            print("have a great day!")
            break
        elif choice == "resources":
            print(f"Bread:{resources['bread']} slice(s) "
                  f"Ham: {resources['ham']} slice(s) "
                  f"Cheese: {resources['cheese']} slice(s)")
        elif choice == "small" or choice == "medium" or choice == "large":
            if sandwich_maker_instance.check_resources(recipes.get(choice).get("ingredients")) == True:
                if cashier_instance.transaction_result(cashier_instance.process_coins(), recipes.get(choice).get("cost")) == True:
                    sandwich_maker_instance.make_sandwich(choice, recipes.get(choice).get("ingredients"))
                """get user input/choice here and check resources and process coins and then show transaction result/cost and make the sandwich"""
        else:
            print("Not an option. Please choose an option.")


if __name__ == "__main__":

    main()
