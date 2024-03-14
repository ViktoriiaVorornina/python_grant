# Створіть функцію, яка повертає всі числа Фібоначчі в діапазоні. Функція приймає початок і кінець
# діапазону як параметри. Використовуйте механізм генераторів усередині функції.
#
# Числа Фібоначчі — це послідовність чисел, де кожне наступне число є сумою двох попередніх.
# Послідовність починається з 0 і 1, а наступні числа визначаються за формулою:
#
# F(0) = 0
#
# F(1) = 1
#
# F(n) = F(n-1) + F(n-2), для n > 1.

# def fibonacci_range(start, end):
#     a, b = 0, 1
#     if end < start:
#         start, end = end, start
#     while a <= end:
#         if a >= start:
#             yield a
#         a, b = b, a + b
#
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))
#
# fibonacci_numbers = list(fibonacci_range(start, end))
# print("Числа Фібоначчі в діапазоні від", start, "до", end, ":", fibonacci_numbers)

# Створіть функцію, яка повертає суму значень елементів списків. Функція приймає два списки. Використовуйте механізм генераторів усередині функції.
# Наприклад, якщо у нас є такі списки:
# 1 3 4 2
# 8 3 5 9
# Результат буде:
# 9 6 9 11
# Якщо передані списки різної довжини, відсутні елементи необхідно вважати рівними нулю.

# def sum_list(list1, list2):
#     len1, len2 = len(list1), len(list2)
#     max_len = max(len1, len2)
#     list1 += [0] * (max_len - len1)
#     list2 += [0] * (max_len - len2)
#
#     ls3 = [list1[i] + list2[i] for i in range(max_len)]
#     return ls3
#
# ls1 = [10,9,8,7]
# ls2 = [1,2,3,4,5]
#
# print(sum_list(ls1, ls2))

# Для виконання цього завдання обов('язково використовуйте механізм функцій вищого порядку (higher order functions).
# Створіть функцію, що зводить значення списку до квадрата або до куба. Користувач визначає, що потрібно зробити (квадрат
# або куб).)
# Сигнатура функції:
# def calculate(list_to_work, function_to_call)
# list_to_work — список з елементами.
# function_to_call — функція для модифікації значень (функція для зведення значень у квадрат або функція для зведення
# значень у куб).


#!!! зводить значення до... яким чином зводить??? перше зроблено просто робить значення квадратичними чи кубічними.
# другий малює квадрат або куб по сумі елементів (сума елементів визначає кількість зірочок)
# !!! Не знаю як зробити об'ємний куб...


# def calculate(list_to_work, function_to_call):
#     return [function_to_call(x) for x in list_to_work]
# def square(x):
#     return x ** 2
# def cube(x):
#     return x ** 3
#
# nums = [1, 2, 3, 4, 5]
#
# options = int(input("Оберіть 1 - для квадрата, 2 - для куба: "))
# if options ==1:
#     print(calculate(nums, square))
# elif options ==2:
#     print(calculate(nums, cube))
# else:
#     print("Невірна опція!")


# def calculate_and_draw(list_to_work, function_to_call):
#     total = sum(list_to_work)
#     function_to_call(total)
# def draw_square(stars):
#     for i in range(stars):
#         print('* ' * stars)
#
# def draw_cube(stars):
#     for i in range(stars):
#         draw_square(stars)
#
# nums = [3, 4, 2, 5]
#
# options = int(input("Введіть 1 для побудови квадрата, 2 -   куба відповідно: "))
# if options == 1:
#     calculate_and_draw(nums, draw_square)
# elif options == 2:
#     calculate_and_draw(nums, draw_cube)
# else:
#     print("Невірна опція!")


# Щороку ваша компанія надає різним державним організаціям фінансову звітність. Залежно від організації формати звітності
# різні. Використовуючи механізм декораторів, вирішіть питання звітності для організацій.

def format_rapport(type_of_org):
    def decorator(func):
        def wrapper(organization):
            if type_of_org == "ФОП":
                print(f"Організація {organization} (тип: {type_of_org}) надає звітність у форматі Excel")
            elif type_of_org == "ТОВ":
                print(f"Організація {organization} (тип: {type_of_org}) надає звітність у форматі CSV")
            else:
                print(f"Організація {organization} (тип: {type_of_org}) надає звітність у форматі PDF")
            func(organization)
        return wrapper
    return decorator

@format_rapport("ФОП")
def generate_financial_report(organization):
    return None

generate_financial_report("ПП Іваненко")

@format_rapport("ТОВ")
def generate_financial_report(organization):
    return None
generate_financial_report("ТОВ Ромашка")

@format_rapport("Інше")
def generate_financial_report(organization):
    return None

generate_financial_report("Компанія XYZ")

