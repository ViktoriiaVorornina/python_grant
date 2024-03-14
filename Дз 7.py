#Користувач вводить з клавіатури рядок. Перевірте, чи є
# введений рядок паліндромом. Паліндроми — слова, речення
# або текст, які однаково читаються як зліва направо, так і
# справа наліво.

# line = input("Введіть рядок: ")
# if line.upper().replace(" ", "") == line[::-1].upper().replace(" ", ""):
#     print("Рядок - паліндром")
# else:
#     print("Рядок - не паліндром")


# Користувач вводить з клавіатури деякий текст, а потім —
# список зарезервованих слів. Знайдіть в тексті всі зарезервовані слова та змініть їх регістр на верхній.
# Виведіть на екран змінений текст.

# line = input("Введіть текст: ")
# words = input("Введіть слова через пробіл: ").split()
# print(words)
#
#
# for i in range(len(words)):
#     words[i] = words[i].lower()
#
# for word in words:
#     if word.lower() in line.lower():
#         line = line.replace(word, word.upper())
#         line = line.replace(word.capitalize(), word.upper())
#
# print(line)



# Маємо певний текст. Підрахуйте кількість пропозицій у
# # цьому тексті та виведіть на екран отриманий результат.
#
text = ("The 1920s was an exciting time for inventions. Some of the things "
        "invented around that time changed the lives of millions of people "
        "and some of those inventions are still widely used today! Some of the things?")
count = 0
for i in text:
    if i == "." or i == "?" or i == "!":
        count += 1

print(f"Текст складається з {count} речень.")

