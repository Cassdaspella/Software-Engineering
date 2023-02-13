class cashier:
    def __init__(self):
            pass
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