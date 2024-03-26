# Створіть клас «Дріб». Збережіть у класі чисельник та знаменник. Реалізуйте методи класу для введення-виведення даних.
# Також створіть методи класу для виконання арифметичних операцій (додавання, віднімання, множення, ділення і т. д.).
# До вже реалізованого класу «Дріб» додайте статичний метод, який при виклику повертає кількість створених об’єктів
# класу «Дріб».

class Fraction:
    num_instances = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.num_instances += 1
        self.reduce()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        common_divisor = self.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    @staticmethod
    def add(fraction1, fraction2):
        new_numerator = fraction1.numerator * fraction2.denominator + fraction2.numerator * fraction1.denominator
        new_denominator = fraction1.denominator * fraction2.denominator
        return Fraction(new_numerator, new_denominator)

    @staticmethod
    def subtract(fraction1, fraction2):
        new_numerator = fraction1.numerator * fraction2.denominator - fraction2.numerator * fraction1.denominator
        new_denominator = fraction1.denominator * fraction2.denominator
        return Fraction(new_numerator, new_denominator)

    @staticmethod
    def multiply(fraction1, fraction2):
        new_numerator = fraction1.numerator * fraction2.numerator
        new_denominator = fraction1.denominator * fraction2.denominator
        return Fraction(new_numerator, new_denominator)

    @staticmethod
    def divide(fraction1, fraction2):
        new_numerator = fraction1.numerator * fraction2.denominator
        new_denominator = fraction1.denominator * fraction2.numerator
        return Fraction(new_numerator, new_denominator)

    @staticmethod
    def get_num_instances():
        return Fraction.num_instances

numerator1 = int(input("Enter numerator for fraction 1: "))
denominator1 = int(input("Enter denominator for fraction 1: "))
fraction1 = Fraction(numerator1, denominator1)

numerator2 = int(input("Enter numerator for fraction 2: "))
denominator2 = int(input("Enter denominator for fraction 2: "))
fraction2 = Fraction(numerator2, denominator2)

result_addition = Fraction.add(fraction1, fraction2)
result_subtraction = Fraction.subtract(fraction1, fraction2)
result_multiplication = Fraction.multiply(fraction1, fraction2)
result_division = Fraction.divide(fraction1, fraction2)
print("Result of addition:", result_addition)
print("Result of subtraction:", result_subtraction)
print("Result of multiplication:", result_multiplication)
print("Result of division:", result_division)

print("Number of Fraction:", Fraction.get_num_instances())

# Створіть клас для конвертування температури з Цельсія
# у Фаренгейт, і навпаки. У класі має знаходитися два статичні
# методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати
# кількість підрахунків температури та повернути це значення
# статичним методом.

# class TemperatureConverter:
#     num_conversions = 0
#
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         fahrenheit = (celsius * 9 / 5) + 32
#         TemperatureConverter.num_conversions += 1
#         return fahrenheit
#
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         celsius = (fahrenheit - 32) * 5 / 9
#         TemperatureConverter.num_conversions += 1
#         return celsius
#
#     @staticmethod
#     def get_num_conversions():
#         return TemperatureConverter.num_conversions
#
# celsius_temperature = 100
# fahrenheit_temperature = TemperatureConverter.celsius_to_fahrenheit(celsius_temperature)
# print(f"{celsius_temperature} Celsius is equal to {fahrenheit_temperature} Fahrenheit")
#
# fahrenheit_temperature = 77
# celsius_temperature = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temperature)
# print(f"{fahrenheit_temperature} Fahrenheit is equal to {celsius_temperature} Celsius")
#
# print("Number of temperature conversions:", TemperatureConverter.get_num_conversions())


# Створіть клас для конвертування з метричної системи в
# англійську, та навпаки. Реалізуйте функціональність у вигляді
# статичних методів. Обов’язково реалізуйте конвертування
# заходів довжини.

# class LengthConverter:
#     @staticmethod
#     def meters_to_feet(meters):
#         feet = meters * 3.28084
#         return feet
#
#     @staticmethod
#     def feet_to_meters(feet):
#         meters = feet / 3.28084
#         return meters
#
#     @staticmethod
#     def kilometers_to_miles(kilometers):
#         miles = kilometers * 0.621371
#         return miles
#
#     @staticmethod
#     def miles_to_kilometers(miles):
#         kilometers = miles / 0.621371
#         return kilometers
#
# meters_length = 100
# feet_length = LengthConverter.meters_to_feet(meters_length)
# print(f"{meters_length} meters is equal to {feet_length} feet")
#
# feet_length = 328
# meters_length = LengthConverter.feet_to_meters(feet_length)
# print(f"{feet_length} feet is equal to {meters_length} meters")
#
# kilometers_length = 10
# miles_length = LengthConverter.kilometers_to_miles(kilometers_length)
# print(f"{kilometers_length} kilometers is equal to {miles_length} miles")
#
# miles_length = 6
# kilometers_length = LengthConverter.miles_to_kilometers(miles_length)
# print(f"{miles_length} miles is equal to {kilometers_length} kilometers")
