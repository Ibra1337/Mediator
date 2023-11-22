
import random

class Order:
    GID = 1

    def __init__(self):
        self.meal_amount = {}
        self.id = Order.GID
        Order.GID += 1

        self.generate_random_meals()

    def generate_random_meals(self):
        total_meals = 10
        possible_meals = ["Spaghetti Bolognese", "Chicken Alfredo", "Vegetarian Pizza", "Grilled Salmon", "Caesar Salad"]

        for _ in range(random.randint(1,total_meals)):

            meal_amount = random.randint(0, 5)
            if meal_amount ==0 :
                continue
            meal_name = random.choice(possible_meals)
            self.addMeal(meal_name, meal_amount)

    def addMeal(self, name: str, amount: int):
        self.meal_amount[name] = amount

    def timeToPrepare(self) -> int:
        res = 0
        for meal in self.meal_amount:
            res += len(meal) * 2 * self.meal_amount[meal]
        return res

