# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас
# CoffeeMachine (містить інформацію про кавомашину), клас
# Blender (містить інформацію про блендер), клас MeatGrinder
# (містить інформацію про м’ясорубку).
# Кожен із класів має містити необхідні для роботи методи.

# class Device:
#
#     def __init__(self, brand, year, puissance):
#         self.brand = brand
#         self.year = year
#         self.puissance = puissance
#
#     def __str__(self):
#         return f"Device: {self.brand} was fabricated in {self.year} and have {self.puissance} W."
#
# class CoffeeMachine(Device):
#     def __init__(self, brand, year, puissance, litres_per_month):
#         super().__init__(brand, year, puissance)
#         self.litres_per_month = litres_per_month
#
#     def __str__(self):
#         return super().__str__() + f" and consume {self.litres_per_month} litres per month."
# class Blender(Device):
#     def __init__(self, brand, year, puissance, outils):
#         super().__init__(brand, year, puissance)
#         self.outils = outils
#
#     def __str__(self):
#         return super().__str__() + f" and have {self.outils} outils in complect."
#
# coffee_machine = CoffeeMachine("CoffeeMaster", 2023, 1200, 20)
# print(coffee_machine)
#
# blender = Blender("BlendX", 2022, 800, 4)
# print(blender)

# Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас
# Frigate (містить інформацію про фрегат), клас Destroyer (містить
# інформацію про есмінця), клас Cruiser (містить інформацію
# про крейсер).
# Кожен із класів має містити необхідні для роботи методи.


# class Ship:
#     def __init__(self, name, length, width, height):
#         self.name = name
#         self.length = length
#         self.width = width
#         self.height = height
#
#
#     def __str__(self):
#         return f"Ship: {self.name} has a length of {self.length}m and a width of {self.width}m and a height of {self.height} m"
#
# class Frigate(Ship):
#
#         def __init__(self, name, length, width, height, year_fabrication):
#             super().__init__(name, length, width, height)
#             self.year_fabrication = year_fabrication
#
#         def __str__(self):
#             return super().__str__() + f" and was fabricated in {self.year_fabrication}."
#
# class Destroyer(Ship):
#     def __init__(self, name, length, width, height, number_of_trip):
#         super().__init__(name, length, width, height)
#         self.number_of_trip = number_of_trip
#
#     def __str__(self):
#         return super().__str__() + f" and has {self.number_of_trip} trips."
#
# sudno = Destroyer("Sudno1", 20, 10, 15, 44)
# print(sudno)

# Запрограмуйте клас Money (об’єкт класу оперує однією
# валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої
# частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання
# значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
# зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.


class Money:

    def __init__(self, currency_unit, ticket, monnaie):
        self.currency_unit = currency_unit
        self.ticket = ticket
        self.monnaie = monnaie
    def __str__(self):
        return f" {self.ticket} {self.currency_unit} {self.monnaie}"

class Product(Money):
    def __init__(self, currency_unit, ticket, monnaie, product):
        super().__init__(currency_unit, ticket, monnaie)
        self.product = product

    def __str__(self):
        return f" this {self.product} cost" + super().__str__()

    def reduce(self, number):
        price = int(f"{self.ticket}{self.monnaie}")
        price -= number

        self.ticket = price // 100
        self.monnaie = price % 100

product1 = Product("USD", 15, 75, "The")
print(product1)
product1.reduce(50)
print(product1)