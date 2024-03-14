# #Користувач вводить з клавіатури арифметичний вираз.
# Наприклад, 23+12.
# Виведіть результат виразу на екран. У нашому прикладі 35.
# Арифметичний вираз може складатися тільки з трьох частин:
# число, операція, число. Можливі операції: +, -, *, /.

# Перший варіант з економією часу))
# expression = input("Введіть вираз:")
# print(eval(expression))

#Другий варіант з використанням патернів
# import re
#
# expression = input("Введіть арифметичний вираз: ")
# pattern = re.compile(r'(\d+)\s*([\+\-\*/])\s*(\d+)')
# match = pattern.match(expression)
#
# if match:
#     num1, operation, num2 = match.groups()
#     result = eval(f"{num1} {operation} {num2}")
#     print("Результат:", result)
# else:
#     print("Неправильний формат виразу.")




# У списку цілих, заповненому випадковими числами, визначте мінімальний та максимальний елементи, підрахуйте
# кількість від’ємних елементів, додатних елементів та кількість
# нулів. Результати виведіть на екран.
from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(-100, 100))
print(numbers)

min = numbers[0]
max = numbers[0]
zero = 0
dodatne = 0
videmne = 0
for i in range(len(numbers)):
    if numbers[i] < min:
        min = numbers[i]
    elif numbers[i] > max:
        max = numbers[i]
    elif numbers[i] == 0:
        zero += 1
    elif numbers[i] > 0:
        dodatne += 1
    elif numbers[i] < 0:
        videmne += 1
print(f"Мінімальне число = {min}")
print(f"Максимальне число = {max}")
print(f"Кількість нулів = {zero}")
print(f"Кількість від'ємних чисел = {videmne}")
print(f"Кількість додатніх чисел = {dodatne}")