# Завдання 1
# Реалізуйте клас «Автомобіль». Збережіть у класі: назву
# моделі, рік випуску, виробника, об’єм двигуна, колір машини,
# ціну. Реалізуйте методи класу для введення-виведення даних
# та інших операцій.

# class Car:
#     def __init__(self, name, year, fabricant, volume, color, price):
#         self.name = name
#         self.year = year
#         self.fabricant = fabricant
#         self.volume = volume
#         self.color = color
#         self.price = price
#
#     def print_car_info(self):
#         print(f" Car {self.name} was fabricated in {self.year} in {self.fabricant},it has {self.volume} horse forces, is {self.color} and cost {self.price} dollars")
#
#     def age_of_car(self, year):
#         print(f"Car is {2024 - self.year} years old")
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# car1 = Car("bmw", 2005, "Germany", 230, "black", 45000)
# car1.print_car_info()
# car1.age_of_car(2005)
# car1.change_color("red")
# car1.print_car_info()

# Завдання 2
# Реалізуйте клас «Книга». Збережіть у класі: назву книги,
# рік видання, видавця, жанр, автора, ціну. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.

# class Book:
#     def __init__(self, name, year, author, genre, price):
#         self.name = name
#         self.year = year
#         self.author = author
#         self.genre = genre
#         self.price = price
#
#     def print_book_info(self):
#         print(f"Book {self.name} was published in {self.year} by {self.author}, it is {self.genre} and cost {self.price} dollars")
#
#     def dollars_to_hryvna(self, price):
#         print(f" Книга за сьогоднішнім курсом коштує {self.price * 39} грн")
#
# book1 = Book("To Kill a Mockingbird", 1960, "Harper Lee", "Роман", 12.50)
# book1.print_book_info()
# book1.dollars_to_hryvna(12.50)

# Завдання 3
# Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Stade:
    def __init__(self, name, date, country, city, area):
        self.name = name
        self.__date = date
        self.country = country
        self.__city = city
        self.area = area

    def info(self):
        print(f"Stade {self.name} was founded in {self.__date} in {self.country}, it is located in {self.__city} "
              f"and has {self.area} square meters")

    # Не знала,що придумати з цим набором даних, буде як дістатися до того стадіону з вашого міста.

    def distance(self, your_city, city):
        import googlemaps
        key_api = "AIzaSyA6UOXGSqduY3BAetWukKOi2iuHBs8Egmw"
        gmaps = googlemaps.Client(key=key_api)
        distance_matrix = gmaps.distance_matrix(your_city, city, mode="driving")
        distance_km = distance_matrix["rows"][0]["elements"][0]["distance"]["value"] / 1000
        print(f"Distance between {self.__city} and {your_city} is {distance_km} km")

stade1 = Stade("Стад де Франс", "24 травня 1998", "Франція", "Сен-Дені", "1.2 мільйона квадратних метрів")
stade1.info()
stade1.distance("Ukraine", "France")
