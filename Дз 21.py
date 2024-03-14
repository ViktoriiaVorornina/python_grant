# Завдання 1
# Маємо текстовий файл. Створіть новий файл, прибравши з нього всі неприйнятні слова. Список неприйнятних
# слів міститься в іншому файлі.

# def del_mots(file1, file2, file_result):
#     try:
#         with open(file1, "r") as f1:
#             text = f1.read()
#             with open(file2, "r") as f2:
#                 unacceptable_words = set(f2.read().split(","))
#                 for word in unacceptable_words:
#                     text = text.replace(word, "")
#             with open(file_result, "w") as f3:
#                 f3.write(text)
#
#     except Exception as e:
#         print(str(e))
#
# del_mots("text_file.txt", "text_file2.txt", "file_result.txt")


# Завдання 2
# Напишіть програму транслітерації з російської на
# англійську, та навпаки. Візьміть дані для транслітерації
# з одного файлу і запишіть їх до іншого. Мовну пару встановлює користувач у меню.


# def translit(input_file, output_file):
#     try:
#         with open(input_file, "r") as f_in:
#             english_words = f_in.read().splitlines()
#             with open(output_file, "a", encoding="utf-8") as f_out:
#                 for english_word in english_words:
#                     russian_translation = input(f"Введіть російську транслітерацію слова '{english_word}': ")
#                     f_out.write(f"{english_word} - {russian_translation}\n")
#         print("Транслітерація успішна.")
#     except Exception as e:
#         print(str(e))
#
# input_file = "text_file.txt"
# output_file = "text_file2.txt"
# translit(input_file, output_file)


# Завдання 3
# Користувач вводить з клавіатури назви файлів, доки
# він не введе слово «quit». Після завершення введення
# програма має об’єднати вміст усіх внесених назв файлів
# в один.
import os

# def file_union(union_file):
#     while True:
#         filename = input("Введіть назву файлу або 'quit' для завершення: ")
#         if filename.lower() == "quit":
#             break
#         try:
#             with open("file_result.txt", "ab") as wr:
#                 for file in os.listdir():
#                     if os.path.isfile(file):
#                         name, extension = os.path.splitext(file)
#                         if name == filename:
#                             with open(file, "rb") as f:
#                                 file_content = f.read()
#                                 wr.write(file_content)
#         except FileNotFoundError:
#             print(f"Файл з назвою '{filename}' не знайдено.")
#
# file_union("file_result.txt")


# Завдання 4
# Користувач вводить з клавіатури назви файлів, доки
# він не введе слово «quit». Після завершення введення
# програма має записати у підсумковий файл символи, які
# містяться у всіх внесених назвах файлів (символи мають
# бути у кожному файлі).

import os

def file_union(union_file):
    while True:
        filename = input("Введіть назву файлу або 'quit' для завершення: ")
        if filename.lower() == "quit":
            break
        try:
            with open("file_result.txt", "w", encoding="utf-8") as wr:
                for file in os.listdir():
                    if os.path.isfile(file):
                        name, extension = os.path.splitext(file)
                        if name == filename:
                            with open(file, "rb") as f:
                                file_content = f.read()
                                character_count = {}
                                for char in file_content:
                                    if char in character_count:
                                        character_count[char] += 1
                                    else:
                                        character_count[char] = 1
                                for key, value in character_count.items():
                                    character = str(key) #!!! Як перетворити числове відображення на символ?
                                    wr.write(f"{character} - {value}\n")
        except FileNotFoundError:
            print(f"Файл з назвою '{filename}' не знайдено.")

file_union("file_result.txt")




#Класна робота
# import os
# import shutil
#
# def list_files(directory):
#     all_files = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             all_files.append(file_path)
#     return all_files
#
#
# files = list_files('.')  # [f for f in os.listdir('.') if os.path.isfile(f)]
#
# file_types = {}
#
# for file in files:
#     ext = file.split('.')[-1]  # main py
#     if ext not in file_types:
#         file_types[ext] = []
#     file_types[ext].append(file)
#
# for ext, files in file_types.items():
#     dir_name = f"{ext.upper()}Files"
#     if not os.path.exists(dir_name):
#         os.mkdir(dir_name)
#     for file in files:
#         shutil.move(file, os.path.join(dir_name, file))