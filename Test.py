# Користувач вводить число. Визначте кількість цифр у
# цьому числі, підрахуйте їх суму та середнє арифметичне.
# Визначте кількість нулів у цьому числі. Спілкування з
# користувачем реалізуйте через меню.

# number = int(input("Введіть будь-яке число: "))
# action = int(input("Натисніть 1, якщо вивести суму; 2 - середнє арифметичне: "))
#
# print("Кількість цифр = ", len(str(number)))
# sum = 0
# for i in str(number):
#     if number > 0:
#         sum += int(i)
#
# if number > 0:
#     if action == 1:
#         print(sum)
#     elif action == 2:
#         average = sum / len(str(number))
#         print(average)
# else:
#     print("Незрозуміла дія або від'ємне число.")


# Напишіть програму, яка виводить на екран шахівницю
# із заданим розміром клітинки. Наприклад, три:

# Перший варіант (згідно картинці завдання)
# size_chess = int(input("Введіть розмір клітинки: "))
# for i in range(size_chess):
#     for j in range(size_chess):
#         print("***", end="")
#         print("___", end="")
#     print()
# for i in range(size_chess):
#     for j in range(size_chess):
#         print("___", end="")
#         print("***", end="")
#     print()

# Другий варіант (згідно логіці)
# size_chess = int(input("Введіть розмір клітинки: "))
# h = 8
# for i in range(h):
#     for j in range(size_chess):
#         if 0 <= i < 4:
#             print("*" * size_chess, end="")
#             print("_" * size_chess, end="")
#         else:
#             print("_" * size_chess, end="")
#             print("*" * size_chess, end="")
#     print()

from random import randint

# Напишіть програму, яка перевіряє користувача на знання таблиці множення. Програма виводить на екран
# два числа, користувач повинен ввести їх добуток. Розробіть кілька рівнів складності (відрізняються складністю
# та кількістю питань). Виведіть користувачеві оцінку його знань.

# level = int(input("Оберіть рівень складності: 1 - легкий, 2 - середній, 3 -важкий : "))
#
# count = 0
#
# for i in range(5):
#     if level == 1:
#         number1 = randint(1, 10)
#         number2 = randint(1, 10)
#         print(f"Введіть добуток чисел {number1} * {number2} = ")
#         result = int(input())
#         if result == number1 * number2:
#             print("Правильна відповідь.")
#             count += 1
#         elif result != number1 * number2:
#             print("Невірна відповідь. Гра закінчена.")
#             if 0 < count <= 2:
#                 print("Ваша оцінка - 3")
#             elif 3 <= count <= 4:
#                 print("Ваша оцінка - 4")
#             else:
#                 print("Іди зубри таблицю множення.")
#             break
#     if count == 5:
#         print("Ваша оцінка - 5")
#
# for i in range(7):
#     if level == 2:
#         number3 = randint(1, 20)
#         number4 = randint(1, 20)
#         print(f"Введіть добуток чисел {number3} * {number4} = ")
#         result = int(input())
#         if result == number3 * number4:
#             print("Правильна відповідь.")
#             count += 1
#         elif result != number3 * number4:
#             print("Невірна відповідь. Гра закінчена.")
#             if 0 < count <= 3:
#                 print("Ваша оцінка - 3")
#             elif 4 <= count <= 6:
#                 print("Ваша оцінка - 4")
#             else:
#                 print("Іди зубри таблицю множення.")
#             break
#     if count == 7:
#         print("Ваша оцінка - 5")
#
# for i in range(10):
#     if level == 3:
#         number5 = randint(1, 20)
#         number6 = randint(1, 20)
#         print(f"Введіть добуток чисел {number5} * {number6} = ")
#         result = int(input())
#         if result == number5 * number6:
#             print("Правильна відповідь.")
#             count += 1
#         elif result != number5 * number6:
#             print("Невірна відповідь. Гра закінчена.")
#             if 0 < count <= 3:
#                 print("Ваша оцінка - 3")
#             elif 4 <= count <= 8:
#                 print("Ваша оцінка - 4")
#             elif count == 9:
#                 print("Ваша оцінка - 4+")
#             else:
#                 print("Іди зубри таблицю множення.")
#             break
#     if count == 10:
#         print("Ваша оцінка - 5")


# Виведіть на екран ромб із зірочок.
# h = int(input("Введіть висоту ромба: "))
# if h < 3: raise ValueError("Неприйнятне значення висоти")
# for i in range(1, h + 1):
#     print(" " * (h - i) + "*" * (2 * i - 1))
#
# for i in range(h - 1, 0, -1):
#     print(" " * (h - i) + "*" * (2 * i - 1))


# Створіть гру «Вгадай число». Програма визначає число в діапазоні від 1 до 500.
# Користувач намагається його
# вгадати. Після кожної спроби, програма видає підказки –
# більше чи менше число за його загадане. Наприкінці програма видає
# статистику: за скільки спроб вгадано число
# і скільки часу це зайняло. Передбачте вихід якщо введе 0 у разі,
# якщо користувачеві набридло вгадувати число.
import time

number = randint(1, 500)
count = 0
start_time = time.time()

while True:
    guess = int(input("Введіть число: "))
    count += 1
    if guess == number:
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)
        print(f"Вітаємо! Ви вгадали число {number} за {count} спроб. Зайняло це {elapsed_time} секунд.")
        break
    elif guess < number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")
