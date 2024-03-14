# Завдання 1
# Створіть функцію, яка повертає всі непарні числа в діапазоні.
# Функція приймає початок і кінець діапазону як параметри.
# Використовуйте механізм генераторів усередині функції.

# def ne_parni(start, end):
#     return list((num for num in range(start, end + 1) if num % 2 != 0))
#
# start_range = int(input("Start: "))
# end_range = int(input("End: "))
# print(ne_parni(start_range, end_range))


# Створіть функцію, яка повертає всі значення зі списку, що не перебувають у діапазоні, зазначеному користувачем.
# Функція приймає список, початок і кінець діапазону як параметри.
# Використовуйте механізм генераторів усередині функції.

# def diapason(ls, start, end):
#     return list([num for num in ls if num not in range(start, end + 1)])
#
# ls = [1,2,3,4,5,6,7,8,9,10,11,12]
# start_range = int(input("Start: "))
# end_range = int(input("End: "))
# print(diapason(ls,start_range, end_range))


# Для виконання цього завдання обов('язково використовуйте механізм функцій вищого порядку (higher order functions). '
# Створіть функцію, що відображає лінію (горизонтальну або вертикальну) з використанням символу, зазначеного користувачем.
# Користувач визначає символ і яку лінію відображати.)
# Сигнатура функції:
# def show_line(symbol, function_to_call)
# symbol — символ для відображення.
# function_to_call — функція для відтворення лінії
# (вертикальна лінія або горизонтальна лінія, на один тип лінії — одна функція).

# def show_line(symbol, function_to_call):
#     function_to_call()
#
# def vertical_line():
#     for i in range(10):
#         print(symbol)
#     return vertical_line
#
# def horizontal_line():
#     print(symbol * 10)
#     return horizontal_line
#
# symbol = input("Symbol: ")
# line = int(input("Line: 1 - Vertical, 2 - Horizontal: "))
#
# if line == 1:
#     show_line(symbol, vertical_line)
# elif line == 2:
#     show_line(symbol, horizontal_line)


# Створіть функцію, що повертає список з усіма парними числами, від 0 до 100000.
# Використовуючи механізм декораторів, порахуйте скільки секунд знадобилося для обчислення всіх чисел.
# Відобразіть на екран кількість секунд і всі парні числа від 0 до 100 000.

# Додайте до четвертого завдання можливість передавати межі діапазону для пошуку всіх парних чисел.
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції: {execution_time} секунд")
        return result
    return wrapper

@measure_time
def is_even(num1, num2): #для 5 завдання (видалити для 4-го)
    ls = []
    # for i in range (0,100000+1): 4 завдання
    for i in range(num1,num2):
        if i % 2 == 0:
            ls.append(i)
    return ls

number1 = int(input("Number 1 - ")) #для 5 завдання
number2 = int(input("Number 2 - "))
print(is_even(number1, number2)) #видалити для 4-го завдання

