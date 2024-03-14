# Напишіть рекурсивну функцію, яка приймає рядок як аргумент і повертає
# кількість слів у цьому рядку, кількість символів, кількість чисел. Слова у рядку
# відокремлені пробілами. Також напишіть код, який тестує цю функцію на різних рядках.
# Критерії оцінки:
# ● Коректність рекурсивної логіки.
# ● Відсутність нескінченного рекурсивного виклику.
# ● Коректне врахування кількості слів.

#Минуло 3 кола пекла...
def number_words(phrase: str):
    def count(phrase: str, word_count: int, letter_count: int, number_count: int, in_word: bool):
        if phrase == "":
            return word_count, letter_count, number_count

        if phrase[0] == " ":
            if in_word:
                word_count += 1
            return count(phrase[1:], word_count, letter_count, number_count, in_word=False)

        elif phrase[0].isdigit():
            if not in_word:
                number_count += 1
            return count(phrase[1:], word_count, letter_count, number_count, in_word=True)

        else:
            return count(phrase[1:], word_count, letter_count + 1, number_count, in_word=True)

    word_count, letter_count, number_count = count(phrase, 0, 0, 0, in_word=False)

    return f"Слів = {(word_count + 1)-number_count}, букв = {letter_count}, цифр = {number_count}"


letters = input("Введіть рядок: ")
print(number_words(letters))


# Реалізуйте функцію, яка аналізує текст (поданий як рядок) та повертає
# інформацію про кількість унікальних слів, частоту їх використання, та список унікальних
# слів, відсортованих за кількістю їх появи в тексті. Функція має використовувати
# словники для підрахунку частоти та кортежі або множини для зберігання унікальних
# слів. Використовуйте модулі для структурування коду
# ● Ефективне використання колекцій.
# ● Коректне сортування та підрахунок.
# ● Чистота та структура коду.
# ● Робота з модулями для організації коду.


# def analyse(text):
#     words = text.split()
#
#     word_counts = {}
#     for word in words:
#         word_counts[word] = word_counts.get(word, 0) + 1
#
#     unique_words = [(word, count) for word, count in word_counts.items()]
#
#     sorted_unique_words = sorted(unique_words, key=lambda x: x[1], reverse=True)
#
#     return sorted_unique_words
#
#
# text = input("Введіть текст: ")
# print(analyse(text))


# Створіть параметризований декоратор measure_performance, який може
# приймати булевий аргумент verbose. Якщо verbose встановлено в True, декоратор має
# виводити ім'я функції, час її виконання та результат. Якщо verbose встановлено в False,
# декоратор повинен виводити тільки час виконання.
# 2. Створіть функцію generate_numbers, яка приймає кількість чисел і генерує
# список випадкових чисел цієї довжини. Створіть функцію find_number, яка приймає
# список чисел і число для пошуку, і використовує лінійний пошук, щоб визначити, чи є
# число в списку.
# 3. Застосуйте декоратор measure_performance з різними параметрами verbose
# до обох функцій.
# Критерії оцінки:
# ● Коректна реалізація та застосування параметризованого декоратора.
# ● Правильне використання вищих функцій.
# ● Ефективність і правильність функцій generate_numbers та find_number.
# ● Чистота коду та дотримання стандартів оформлення коду Python.
#
# import time
# def measure_performance(verbose: bool):
#     def measure(func):
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             result = func(*args, **kwargs)
#             end_time = time.time()
#             if verbose == True:
#                 print(f"{func.__name__} зайняло {end_time - start_time} часу")
#             else:
#                 print( f"Це зайняло {end_time - start_time} часу")
#             return result
#         return wrapper
#     return measure
#
# from random import randint
#
# @measure_performance(verbose=True)
# def generate_numbers(n: int):
#     return [randint(1, 50) for i in range(n)]
#
# @measure_performance(verbose=False)
# def generate_numbers2(n: int):
#     return [randint(1, 50) for i in range(n)]
#
# @measure_performance(verbose=True)
# def find_number(numbers: list, number: int):
#     for i in numbers:
#         if i == number:
#             return "Цифру знайдено"
#     return "Цифру не знайдено"
# @measure_performance(verbose=False)
# def find_number2(numbers: list, number: int):
#     for i in numbers:
#         if i == number:
#             time.sleep(1) #щоб побачити що це працює, бо швидкість виконання менше долі секунди
#             return "Цифру знайдено"
#     return "Цифру не знайдено"
#
# print(generate_numbers(8))
# print(generate_numbers2(10))
# print(find_number([19,5,34,22,7,16,4], 5))
# print(find_number2([90, 76, 5, 45, 89, 3, 7], 3))