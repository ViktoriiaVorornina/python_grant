# Завдання 2:
#Система замовлення їжі онлайн

import json
import os
class Meal:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price
        }

class Menu:
    def __init__(self, filename):
        self.filename = filename
        self.meals = self.load_menu()

    def load_menu(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                meals_data = json.load(file)
                meals = []
                for meal_data in meals_data:
                    meal = Meal(meal_data["name"], meal_data["category"], meal_data["price"])
                    meals.append(meal)
                return meals
        else:
            return []

    def save_menu(self):
        with open(self.filename, 'w') as file:
            meals_data = [meal.to_dict() for meal in self.meals]
            json.dump(meals_data, file)

    def add_meal(self, meal):
        self.meals.append(meal)

    def remove_meal(self, meal):
        self.meals.remove(meal)

    def update_meal_price(self, meal_name, new_price):
        for meal in self.meals:
            if meal.name == meal_name:
                meal.price = new_price
                break

    def display_menu(self):
        for meal in self.meals:
            print(f"{meal.name} - {meal.category} - ${meal.price}")

    def search_by_category(self, category):
        result = [meal for meal in self.meals if meal.category.lower() == category.lower()]
        if result:
            for meal in result:
                print(f"{meal.name} - {meal.category} - ${meal.price}")
        else:
            print("No meals found in this category.")

    def search_by_name(self, name):
        result = [meal for meal in self.meals if name.lower() in meal.name.lower()]
        if result:
            for meal in result:
                print(f"{meal.name} - {meal.category} - ${meal.price}")
        else:
            print("No meals found with this name.")


class Order:
    def __init__(self):
        self.items = []
        self.status = "Pending"

    def add_item(self, meal):
        self.items.append(meal)

    def remove_item(self, meal):
        if meal in self.items:
            self.items.remove(meal)

    def place_order(self):
        self.status = "Placed"

    def cancel_order(self):
        self.status = "Cancelled"

    def to_dict(self):
        return {
            "items": [meal.__dict__ for meal in self.items],
            "status": self.status
        }

class OrderManager:
    def __init__(self, filename):
        self.filename = filename
        self.orders = self.load_orders()

    def load_orders(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    orders_data = json.load(file)
                    orders = []
                    for order_data in orders_data:
                        order = Order()
                        for item_data in order_data["items"]:
                            meal = Meal(item_data["name"], item_data["category"], item_data["price"])
                            order.add_item(meal)
                        order.status = order_data["status"]
                        orders.append(order)
                    return orders
                except json.decoder.JSONDecodeError:
                    print(f"Error loading orders from {self.filename}. File is empty or not valid JSON.")
                    return []
        else:
            return []

    def save_orders(self):
        orders_to_save = [order.to_dict() for order in self.orders]
        with open(self.filename, 'w') as file:
            json.dump(orders_to_save, file, indent=4)

    def place_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        if order in self.orders:
            self.orders.remove(order)

    def track_order_status(self, order):
        return order.status

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deduct_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def to_dict(self):
        return {
            "name": self.name,
            "balance": self.balance
        }


class UserManager:
    def __init__(self, filename):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    users_data = json.load(file)
                    users = []
                    for user_data in users_data:
                        user = User(user_data["name"], user_data["balance"])
                        users.append(user)
                    return users
                except json.decoder.JSONDecodeError:
                    print(f"Error loading users from {self.filename}. File is empty or not valid JSON.")
                    return []
        else:
            return []

    def save_users(self):
        with open(self.filename, 'w') as file:
            users_to_save = [user.to_dict() for user in self.users]
            json.dump(users_to_save, file)

    def add_user(self, user):
        self.users.append(user)


class PaymentProcessor:
    def process_payment(self, user, amount):
        if user.deduct_balance(amount):
            return True
        else:
            return False

menu_manager = Menu("menu.json")
order_manager = OrderManager("orders.json")
user_manager = UserManager("users.json")
payment_processor = PaymentProcessor()

burger = Meal("Cheeseburger", "Burgers", 5.99)
pasta = Meal("Spaghetti Carbonara", "Pasta", 8.50)

menu_manager.add_meal(burger)
menu_manager.add_meal(pasta)

user1 = User("John", 50)
user2 = User("Alice", 30)

user_manager.add_user(user1)
user_manager.add_user(user2)

order1 = Order()
order1.add_item(burger)
order1.add_item(pasta)
order1.place_order()

order_manager.place_order(order1)

print("Статус замовлення:", order_manager.track_order_status(order1))

print("Баланс користувача до оплати:", user1.balance)
payment_processor.process_payment(user1, 14.49)
print("Баланс користувача після оплати:", user1.balance)

menu_manager.save_menu()
order_manager.save_orders()
user_manager.save_users()