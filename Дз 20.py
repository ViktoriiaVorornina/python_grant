# Завдання 6
# Маємо текстовий файл. Перепишіть до іншого файлу
# всі його рядки замінюючи в них символ * на символ &, і навпаки

def file(inputfile, outputfile):
    try:
        f = open(inputfile, 'r')
        lines = f.readlines()
        f.close()

        out = open(outputfile, 'w')
        for line in lines:
            updated_line = line.replace('*', 'TEMP_REPLACE').replace('&', '*').replace('TEMP_REPLACE', '&')
            out.write(updated_line)
    except Exception as e:
        print(str(e))

file('text_file.txt', 'text_file2.txt')

#Текст початковий
# Health insurance premiums, which are obligatory for everyone,
# have been & rising fast, and older people sometimes struggle to pay them.
# Women who may have had work breaks * to raise a family,
# and immigrants recruited decades ago to work in Swiss factories, restaurants,
# or hospitals, ** can find it particularly difficult to make ends meet.
# More and more people are working * into their 70s not out & of choice, but out of necessity.
# Meanwhile among the younger ****** generation, work related stress and burnout are increasing.
# The proposal to && increase pensions came from the trades unions - but was opposed by the
# Swiss government, parliament, and && business leaders, who argued it was unaffordable.

# Завдання 7
# Маємо масив рядків. Запишіть їх у файл, розташувавши
# кожен елемент масиву на окремому рядку їз збереженням
# порядку.

# def file(lignes, outputfile):
#     try:
#         with open(outputfile, 'w') as out:
#             for line in lignes:
#                 out.write(line + '\n')
#     except Exception as e:
#         print(str(e))
#
# text = [
#     "Health insurance premiums, which are obligatory for everyone, have been * rising fast, and older people sometimes struggle to pay them.",
#     "Women who may have had work breaks & to raise a family, and immigrants recruited decades ago to work in Swiss factories, restaurants, or hospitals, ** can find it particularly difficult to make ends meet.",
#     "More and more people are working * into their 70s not out & of choice, but out of necessity.",
#     "Meanwhile among the younger ****** generation, work related stress and burnout are increasing.",
#     "The proposal to && increase pensions came from the trades unions - but was opposed by the Swiss government, parliament, and && business leaders, who argued it was unaffordable."
# ]
#
# file(text, 'text_file2.txt')

# Завдання 8
# Маємо масив рядків. Запишіть їх у файл, розташувавши
# кожен елемент масиву на окремому рядку із збереженням
# порядку.

#!!! Це таке ж саме як і 7 завдання.!!!

# Завдання 9
# Маємо текстовий файл. Підрахуйте кількість символів у ньому.

# def file(inputfile):
#     try:
#         count = 0
#         f = open(inputfile, 'r')
#         lines = f.readlines()
#         for line in lines:
#             count += len(line)
#         print("Total characters in the file:", count)
#         f.close()
#         return count
#
#     except Exception as e:
#         print(str(e))
#
# file('text_file.txt')

# Завдання 10
# Маємо текстовий файл. Підрахуйте кількість рядків у ньому

def file(inputfile):
    try:
        count = 0
        f = open(inputfile, 'r')
        lines = f.readlines()
        count = sum(1 for line in lines)
        print("Total characters in the file:", count)
        f.close()
        return count

    except Exception as e:
        print(str(e))

file('text_file.txt')