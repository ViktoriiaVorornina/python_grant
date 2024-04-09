# Завдання 1:
# Створіть функцію відображення поточного часу.
# Функція не приймає параметри та не використовує
# синтаксис декораторів. Зробіть декорування функції за
# допомогою іншого класу-декоратора. Потенційне виведення даних
# на екран:
# ***************************
# 23:00
# ***************************
# У цьому виведенні на екран дві лінії із зірочок — результати декорування.

# class TimeDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print("*" * 27)
#         self.func()
#         print("*" * 27)
#
# def show_current_time():
#     import datetime
#     current_time = datetime.datetime.now().strftime("%H:%M")
#     print(current_time)
#
# current_time = TimeDecorator(show_current_time)
# current_time()

# Завдання 2:
# Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію
# про службовця. Для базового класу це може бути рядок із написом
# «This is Employer class».
# Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
# інформації, що відповідає кожному типу службовця.
# реалізуйте магічний метод str, а також метод int (який повертає вік
# службовця).

# class Employer:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def Print(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#     def __str__(self):
#         return f"Employer {self.name}"
#
#     def __int__(self):
#         return self.age
#
#
# class President(Employer):
#     def Print(self):
#         print(f"This is President class. Name: {self.name}, Age: {self.age}")
#
#     def __str__(self):
#         return f"President {self.name}"
#
#     def __int__(self):
#         return self.age
#
#
# class Manager(Employer):
#     def Print(self):
#         print(f"This is Manager class. Name: {self.name}, Age: {self.age}")
#
#     def __str__(self):
#         return f"Manager {self.name}"
#
#     def __int__(self):
#         return self.age
#
#
# class Worker(Employer):
#     def Print(self):
#         print(f"This is Worker class. Name: {self.name}, Age: {self.age}")
#
#     def __str__(self):
#         return f"Worker {self.name}"
#
#     def __int__(self):
#         return self.age
#
# president = President("John", 50)
# manager = Manager("Alice", 40)
# worker = Worker("Bob", 30)
#
# president.Print()
# print(str(president))
# print(int(president))
#
# manager.Print()
# print(str(manager))
# print(int(manager))
#
# worker.Print()
# print(str(worker))
# print(int(worker))

# Завдання 3: це теж саме, що і друге.

# Завдання 4
# Створіть клас Date, який міститиме інформацію про
# дату (день, місяць, рік). За допомогою механізму перевантаження операторів визначте операцію різниці двох дат
# (результат у вигляді кількості днів між датами), а також
# операцію збільшення дати на певну кількість днів.

from datetime import datetime, timedelta


class Date:
    def __init__(self, day, month, year):
        self.date = datetime(year, month, day)

    def __sub__(self, other):
        difference = abs((self.date - other.date).days)
        return difference

    def __add__(self, days):
        new_date = self.date + timedelta(days=days)
        return new_date.strftime("%d/%m/%Y")

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")

date1 = Date(1, 1, 2024)
date2 = Date(31, 12, 2022)

print("Date 1:", date1)
print("Date 2:", date2)

difference = date1 - date2
print("Difference in days:", difference)

new_date = date1 + 100
print("New date after adding 100 days:", new_date)
