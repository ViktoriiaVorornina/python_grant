# Напишіть функцію для підрахунку добутку елементів
# списку цілих. Список передається як параметр. Отриманий
# результат повертається із функції.

# def dobutok(ls):
#     dob = 1
#     for x in ls:
#         dob *= x
#     return dob
#
# print(dobutok([1, 2, 3,4]))


# Напишіть функцію для знаходження мінімуму в списку
# цілих. Список передається як параметр. Отриманий результат
# повертається із функції

# def minimum(ls):
#     min = ls[0]
#     for i in range(len(ls)):
#         if ls[i] < min:
#             min = ls[i]
#     return min
#
# print(minimum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Напишіть функцію, яка визначає кількість простих чисел
# у списку цілих. Список передається як параметр. Отриманий
# результат повертається із функції

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# def count_primes(numbers):
#     count = 0
#     for num in numbers:
#         if is_prime(num):
#             count += 1
#     return count
#
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(count_primes(numbers))

# Напишіть функцію, яка видаляє зі списку цілих певне
# задане число. З функції потрібно повернути кількість віддалених елементів

# def delete(ls, number):
#     count_left = 0
#     count_right = 0
#     for i in range(len(ls)):
#         if ls[i] != number:
#             count_left += 1
#         else:
#             break
#     for i in range(len(ls) - 1, -1, -1):
#         if ls[i] != number:
#             count_right += 1
#         else:
#             break
#
#     return count_left, count_right
#
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# number = int(input("Введіть число: "))
# print(delete(ls, number))


# Напишіть функцію, яка отримує два списки як параметр
# і повертає список з елементами обох списків.

# def reunir(ls1, ls2):
#     ls3 = list(zip(ls1, ls2))
#     return ls3
#
# ls1 = [1, 2, 3, 4, 5]
# ls2 = [6, 7, 8, 9, 10]
#
# print(reunir(ls1, ls2))

# Напишіть функцію, яка підраховує степінь кожного елемента
# списку цілих. Значення для степеня, як і список, передається
# як параметр. Функція повертає новий список з отриманими
# результатами.

def calculate_powers(ls, power):
    result = []
    for num in ls:
        result.append(num ** power)
    return result

numbers = [1, 2, 3, 4, 5]
exponent = 3
powered_numbers = calculate_powers(numbers, exponent)
print(powered_numbers)




# # Напишіть рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b. Користувач вводить a та b.
# # Покажіть приклад роботи функції.
#
# def sum_range(a, b):
#     if a > b:
#         return 0
#     else:
#         return a + sum_range(a + 1, b)
#
# a = int(input("Введіть початок діапазону: "))
# b = int(input("Введіть кінець діапазону: "))
#
# print(sum_range(a,b))

