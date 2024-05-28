import json

class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class HotDog:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def get_price(self):
        return sum(ingredient.price for ingredient in self.ingredients)

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

class Order:
    def __init__(self, customer, hotdogs):
        self.customer = customer
        self.hotdogs = hotdogs
        self.discount = 0

    def calculate_total(self):
        total = sum(hotdog.get_price() for hotdog in self.hotdogs)
        if len(self.hotdogs) >= 3:
            self.discount = total * 0.10
        return total - self.discount

class Customer:
    def __init__(self, name):
        self.name = name

class HotDogController:
    def __init__(self):
        self.hotdogs = []
        self.recipes = self._load_recipes()

    def _load_recipes(self):
        recipes = [
            Recipe("Classic", [Ingredient("Sausage", 1.0), Ingredient("Bun", 0.5), Ingredient("Ketchup", 3.2)]),
            Recipe("Cheese", [Ingredient("Sausage", 1.0), Ingredient("Bun", 0.5), Ingredient("Cheese", 4.3)]),
            Recipe("Spicy", [Ingredient("Sausage", 1.0), Ingredient("Bun", 0.5), Ingredient("Jalapeno", 5.4)])
        ]
        return recipes

    def create_custom_hotdog(self, name, ingredients):
        hotdog = HotDog(name, ingredients)
        self.hotdogs.append(hotdog)
        return hotdog

    def get_recipes(self):
        return self.recipes

class OrderController:
    def __init__(self):
        self.orders = []

    def create_order(self, customer, hotdogs):
        order = Order(customer, hotdogs)
        self.orders.append(order)
        return order

    def get_total_sales(self):
        return sum(order.calculate_total() for order in self.orders)

    def get_total_hotdogs_sold(self):
        return sum(len(order.hotdogs) for order in self.orders)

class IngredientController:
    def __init__(self):
        self.ingredients = {
            "Sausage": 50,
            "Bun": 50,
            "Ketchup": 50,
            "Cheese": 50,
            "Jalapeno": 50
        }

    def use_ingredient(self, name, quantity):
        if self.ingredients[name] >= quantity:
            self.ingredients[name] -= quantity
        else:
            raise ValueError(f"Not enough {name}")

    def get_ingredient_stock(self):
        return self.ingredients

    def get_low_stock_ingredients(self):
        return {name: qty for name, qty in self.ingredients.items() if qty < 10}

class ConsoleInterface:
    def __init__(self, hotdog_controller, order_controller, ingredient_controller):
        self.hotdog_controller = hotdog_controller
        self.order_controller = order_controller
        self.ingredient_controller = ingredient_controller

    def run(self):
        while True:
            print("1. Choose standard hot-dog recipe")
            print("2. Create custom hot-dog")
            print("3. View total sales")
            print("4. View total hot-dogs sold")
            print("5. View ingredient stock")
            print("6. View low stock ingredients")
            print("7. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.choose_standard_hotdog()
            elif choice == "2":
                self.create_custom_hotdog()
            elif choice == "3":
                self.view_total_sales()
            elif choice == "4":
                self.view_total_hotdogs_sold()
            elif choice == "5":
                self.view_ingredient_stock()
            elif choice == "6":
                self.view_low_stock_ingredients()
            elif choice == "7":
                break

    def choose_standard_hotdog(self):
        recipes = self.hotdog_controller.get_recipes()
        for idx, recipe in enumerate(recipes):
            print(f"{idx + 1}. {recipe.name} - {', '.join(ingredient.name for ingredient in recipe.ingredients)}")

        choice = int(input("Select a recipe: ")) - 1
        selected_recipe = recipes[choice]
        customer_name = input("Enter your name: ")
        customer = Customer(customer_name)
        hotdog = HotDog(selected_recipe.name, selected_recipe.ingredients)
        order = self.order_controller.create_order(customer, [hotdog])
        print(f"Your order: {selected_recipe.name} - Total: ${order.calculate_total()}")
        self._save_order(order)

    def create_custom_hotdog(self):
        name = input("Enter custom hot-dog name: ")
        ingredients = []

        while True:
            ingredient_name = input("Enter ingredient (or 'done' to finish): ")
            if ingredient_name == "done":
                break
            if ingredient_name in self.ingredient_controller.get_ingredient_stock():
                ingredient = Ingredient(ingredient_name, 5.5)
                ingredients.append(ingredient)
                self.ingredient_controller.use_ingredient(ingredient_name, 1)
            else:
                print(f"Ingredient {ingredient_name} not available")

        customer_name = input("Enter your name: ")
        customer = Customer(customer_name)
        hotdog = HotDog(name, ingredients)
        order = self.order_controller.create_order(customer, [hotdog])
        print(f"Your order: {name} - Total: ${order.calculate_total()}")
        self._save_order(order)

    def view_total_sales(self):
        total_sales = self.order_controller.get_total_sales()
        print(f"Total sales: ${total_sales}")

    def view_total_hotdogs_sold(self):
        total_hotdogs_sold = self.order_controller.get_total_hotdogs_sold()
        print(f"Total hot-dogs sold: {total_hotdogs_sold}")

    def view_ingredient_stock(self):
        stock = self.ingredient_controller.get_ingredient_stock()
        for ingredient, quantity in stock.items():
            print(f"{ingredient}: {quantity}")

    def view_low_stock_ingredients(self):
        low_stock = self.ingredient_controller.get_low_stock_ingredients()
        for ingredient, quantity in low_stock.items():
            print(f"{ingredient}: {quantity}")

    def _save_order(self, order):
        with open("orders.json", "a") as file:
            order_data = {
                "customer": order.customer.name,
                "hotdogs": [{"name": hotdog.name, "ingredients": [ingredient.name for ingredient in hotdog.ingredients]} for hotdog in order.hotdogs],
                "total": order.calculate_total()
            }
            json.dump(order_data, file)
            file.write("\n")

hotdog_controller = HotDogController()
order_controller = OrderController()
ingredient_controller = IngredientController()

console_interface = ConsoleInterface(hotdog_controller, order_controller, ingredient_controller)
console_interface.run()
