class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
        }

    def report(self):
        """Prints a report of all resources"""
        for key, item in self.resources.items():
            print(f'{key}: {item}ml' if key != "coffee" else f'{key}: {item}g')

    def is_resource_sufficient(self, drink):
        """Checks if you have enough resources for a drink to be made"""
        for ingredient, amount in drink.ingredient.items():
            if self.resources.get(ingredient, 0) < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, drink):
        """Deducts the required ingredients from resources"""
        for ingredient, amount in drink.ingredient.items():
            self.resources[ingredient] -= amount
        print(f"Here's your {drink.name} ☕. Enjoy!")
