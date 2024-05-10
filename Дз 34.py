# Завдання 1
# Реалізуйте патерн Builder. Протестуйте роботу створеного
# класу.

class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_year(self, year):
        self.car.year = year
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car


class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_sports_car(self):
        return self.builder.set_make("Ferrari").set_model("488 GTB").set_year(2022).set_color("Red").build()

    def construct_suv(self):
        return self.builder.set_make("Jeep").set_model("Grand Cherokee").set_year(2023).set_color("Black").build()

builder = CarBuilder()
director = CarDirector(builder)

sports_car = director.construct_sports_car()
print("Sports car:", sports_car)

suv = director.construct_suv()
print("SUV:", suv)

# Завдання 2
# Створіть додаток для приготування пасти. Додаток має
# вміти створювати щонайменше три види пасти. Класи різної
# пасти мають містити такі методи:
# ■ Тип пасти;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реалізації використовуйте твірні патерни.

class Pasta:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.topping = None
        self.extras = []

    def __str__(self):
        description = f"Type: {self.type}\nSauce: {self.sauce}\nTopping: {self.topping}\nExtras: {', '.join(self.extras)}"
        return description


class PastaFactory:
    def create_pasta(self, pasta_type):
        if pasta_type == "Spaghetti":
            return Spaghetti()
        elif pasta_type == "Penne":
            return Penne()
        elif pasta_type == "Fettuccine":
            return Fettuccine()
        else:
            raise ValueError("Invalid pasta type")


class Spaghetti(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Spaghetti"
        self.sauce = "Tomato"
        self.topping = "Parmesan"
        self.extras = ["Basil", "Olive oil"]


class Penne(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Penne"
        self.sauce = "Alfredo"
        self.topping = "Mozzarella"
        self.extras = ["Chicken", "Broccoli"]


class Fettuccine(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Fettuccine"
        self.sauce = "Pesto"
        self.topping = "Pine nuts"
        self.extras = ["Shrimp", "Cherry tomatoes"]

factory = PastaFactory()

spaghetti = factory.create_pasta("Spaghetti")
print("Spaghetti:")
print(spaghetti)

penne = factory.create_pasta("Penne")
print("\nPenne:")
print(penne)

fettuccine = factory.create_pasta("Fettuccine")
print("\nFettuccine:")
print(fettuccine)

# Завдання 3
# Реалізуйте патерн Prototype. Протестуйте роботу створеного класу.

import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj


class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


prototype = Prototype()
car_prototype = Car()
car_prototype.make = "Ford"
car_prototype.model = "Focus"
car_prototype.year = 2019
prototype.register_object("Car", car_prototype)

car_clone = prototype.clone("Car", year=2022)
print(car_clone)
