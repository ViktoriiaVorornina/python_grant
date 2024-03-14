# Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх елементів більше за нуль;
# якщо ні — тільки першу третину. Решту списку не сортуйте,
# а розташуйте у зворотному порядку

from random import randint
#Варіант для лінивих))
# #list = [34, 5, 8, 0, -3, 9, 2, 44, -7, 98, 33, 65]
# list = [randint(-20, 20) for i in range(12)]
# print(list, sum(list)//len(list))
# result = []
# for i in enumerate(list):
#     if sum(list)//len(list) > 0:
#         result = sorted(list[0:(len(list)//3)*2])
#         result = result + list[len(list)//3*2:][::-1]
#     elif sum(list)//len(list) <= 0:
#         result = sorted(list[0:(len(list)//3)])
#         result = result + list[len(list)//3:][::-1]
#
# print(result)

#Варіант сортування:
# list = [randint(-20, 20) for i in range(12)]
# print(list, sum(list)//len(list))
# result = []
#
#
# if sum(list)//len(list) > 0:
#     for j in range(0, (len(list)//3)*2):
#         for i in range(0, len(list)//3*2 - 1):
#             if list[i] > list[i + 1]:
#                 list[i + 1], list[i] = list[i], list[i + 1]
#         result = list[0:len(list)//3*2] + list[len(list)//3*2:][::-1]
# elif sum(list) // len(list) <= 0:
#     for j in range(0, (len(list)//3)):
#         for i in range(0, len(list)//3 - 1):
#             if list[i] > list[i + 1]:
#                 list[i + 1], list[i] = list[i], list[i + 1]
#         result = list[0:len(list)//3] + list[len(list)//3:][::-1]
#
# print("Відсортований список:", result)


# Написати програму «Успішність». Користувач вводить
# 10 оцінок студента. Оцінки від 1 до 12. Реалізуйте меню для
# користувача:
# ■ виведення оцінок (виведення вмісту списку);
# ■ перескладання іспиту (користувач вводить номер елемента
# списку та нову оцінку);
# ■ отримання стипендії (стипендію отримують, якщо середній бал не нижче 10.7);
# ■ виведення відсортованого списку оцінок: за зростанням
# або спаданням.

# list_notes = []
# for i in range(1, 11):
#     notes = int(input(f"Введіть {i:} оцінку студента: "))
#     if 0 < notes <= 12:
#         list_notes.append(notes)
#     else:
#         print("Введене значення недопустиме")
# print("Виведення оцінок: ", list_notes)
# options = int(input("Натисніть 1 для перескладання іспиту, 2 - для визначення стипендії,3 - для виведення відсортованих "
#                     "оцінок за зростанням, 4 - виведення відсортованих оцінок за спаданням: "))
# if options == 1:
#     number_notes = int(input("Введіть номер оцінки яку хочете змінити: "))
#     list_notes[number_notes-1] = int(input("Введіть нову оцінку: "))
#     print("Новий список оцінок після перескладання іспиту: ", list_notes)
# elif options == 2:
#     if sum(list_notes)/len(list_notes) >= 10.7:
#         print(f"Середня оцінка студента = {sum(list_notes)/len(list_notes)} - Він заслуговує на стипендію.")
#     elif sum(list_notes)/len(list_notes) <= 10.7:
#         print(f"Середня оцінка студента = {sum(list_notes)/len(list_notes)} - Він не заслуговує на стипендію.")
# elif options == 3:
#     for i in range(len(list_notes)):
#         min_index = i
#         for j in range(i + 1, len(list_notes)):
#             if list_notes[j] < list_notes[min_index]:
#                 min_index = j
#         list_notes[i], list_notes[min_index] = list_notes[min_index], list_notes[i]
#     print("Відсортований список оцінок за зростанням: ", list_notes)
# elif options == 4:
#     for i in range(len(list_notes)):
#         max_index = i
#         for j in range(i + 1, len(list_notes)):
#             if list_notes[j] > list_notes[max_index]:
#                 max_index = j
#         list_notes[i], list_notes[max_index] = list_notes[max_index], list_notes[i]
#     print("Відсортований список оцінок за зростанням: ", list_notes)
# else:
#     print("Обраної опції не існує")


# Напишіть програму для сортування списку методом
# удосконаленого бульбашкового сортування. Удосконалення
# полягає в тому, щоб аналізувати кількість перестановок на
# кожному кроці. Якщо ця кількість дорівнює нулю, то продовжувати сортування немає сенсу — список відсортовано.

my_list = [randint(-20, 20) for i in range(12)]
#my_list = [1,2,3,4,5,6,7,8,9,10,11]
print("Початковий список:", my_list)

n = len(my_list)
total_swaps = 0
for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            swapped = True
            total_swaps += 1
    if total_swaps == 0:
        break

print("Відсортований список:", my_list)
print("Загальна кількість перестановок:", total_swaps)


