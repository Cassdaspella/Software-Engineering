
class sandwich_maker:
    def __init__(self, resources):
        self.machine_resources = resources
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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
            Hint: no output"""
        for ingredients in order_ingredients:
            self.machine_resources.update(
                {ingredients: self.machine_resources.get(ingredients) - order_ingredients.get(ingredients)})

            DB_HOST = "localhost"
            DB_NAME = "sandwich_maker"
            DB_USERNAME = "root"
            DB_Password = "rootroot"