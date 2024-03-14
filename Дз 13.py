# Завдання 1
# Створіть програму, що містить інформацію про відомих
# баскетболістів. Збережіть ПІБ та зріст кожного баскетболіста. Реалізуйте можливість додавати, видаляти, знаходити та
# змінювати дані. Використовуйте словник для збереження
# інформації.


# basket = [{"lastname": "Trishchuk", "firstname": "Denys", "patronyme": "Vitaliyovich", "mesure": "170"},
#           {"lastname": "Skoryk", "firstname": "Anna", "patronyme": "Evgeniivna", "mesure": "182"},
#           {"lastname": "Voronina", "firstname": "Viktoriia", "patronyme": "Vitaliivna", "mesure": "170"}]
#
# function = int(input("Натисніть 1, щоб додати, 2 - видалити, 3 - знайти, 4 - змінити дані: "))
#
# if function ==  1:
#     basket.append({"lastname": input("Введіть прізвище: "),
#                     "firstname": input("Введіть ім'я: "),
#                     "patronyme": input("Введіть побатькові: "),
#                     "mesure": input("Введіть зріст: ")})
#     print(basket)
#
# elif function == 2:
#     lastname = input("Введіть прізвище: "),
#     firstname = input("Введіть ім'я: "),
#     patronyme = input("Введіть побатькові: "),
#     for item in basket:
#         if item["lastname"] == lastname and item["firstname"] == firstname and item["patronyme"] == patronyme:
#             basket.remove(item)
#         else:
#             print("Не знайдено")
#
#     print(basket)
#
# elif function == 3:
#     lastname = input("Введіть прізвище: "),
#     firstname = input("Введіть ім'я: "),
#     patronyme = input("Введіть побатькові: "),
#     for item in basket:
#         if item["lastname"] == lastname and item["firstname"] == firstname and item["patronyme"] == patronyme:
#             print(item)
#         else:
#             print("Не знайдено")
#
# elif function == 4:
#     lastname = input("Введіть прізвище: "),
#     firstname = input("Введіть ім'я: "),
#     patronyme = input("Введіть побатькові: "),
#     for item in basket:
#         if item["lastname"] == lastname and item["firstname"] == firstname and item["patronyme"] == patronyme:
#             item["lastname"] = input("Введіть прізвище: ")
#             item["firstname"] = input("Введіть ім'я: ")
#             item["patronyme"] = input("Введіть побатькові: ")
#             item["mesure"] = input("Введіть зріст: ")
#             print(item)
#         else:
#             print("Не знайдено")

# Завдання 2
# Створіть програму «Англо-французький словник». Збережіть слово англійською та його переклад на французьку.
# Реалізуйте можливість додавати, видаляти, знаходити та
# змінювати дані. Використовуйте словник для збереження
# інформації.

# dictionary = [{"day": "jour", "month": "mois", "hello": "salut"}]
#
# function = int(input("Натисніть 1, щоб додати, 2 - видалити, 3 - знайти, 4 - змінити дані: "))
#
# if function == 1:
#     dictionary.append({input("Введіть англ слово: "): input("Введіть франц слово: ")})
#     print(dictionary)
#
# elif function == 2:
#     word = input("Введіть слово англійською:")
#     for words in dictionary:
#         if word in words:
#             del words[word]
#             break
#
#     print(dictionary)
#
# elif function == 3:
#     word = input("Введіть слово англійською:")
#     for words in dictionary:
#         if word in words:
#             print(words)
#         else:
#             print("Не знайдено")
#
# elif function == 4:
#     word = input("Введіть слово англійською:")
#     new_translation = input("Введіть новий переклад для цього слова:")
#     found = False
#     for words in dictionary:
#         if word in words.keys():
#             words[word] = new_translation
#             print("Дані оновлено:", words)
#             found = True
#             break
#     if not found:
#         print("Не знайдено")

#
# Завдання 3
# Створіть програму «Фірма», яка зберігає інформацію про
# працівників: ПІБ, телефон, корпоративний email, назва посади,
# номер кабінету, Skype. Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте словник
# для збереження інформації.


companies = [
    {
        "назва": "Фірма 1",
        "працівники": [
            {
                "ПІБ": "Іванов Іван Іванович",
                "телефон": "123456789",
                "корпоративний email": "ivanov@firm1.com",
                "назва посади": "менеджер",
                "номер кабінету": "101",
                "Skype": "ivanov_skype"
            },
            {
                "ПІБ": "Петров Петро Петрович",
                "телефон": "987654321",
                "корпоративний email": "petrov@firm1.com",
                "назва посади": "бухгалтер",
                "номер кабінету": "102",
                "Skype": "petrov_skype"
            }
        ]
    },
    {
        "назва": "Фірма 2",
        "працівники": [
            {
                "ПІБ": "Сидоров Олег Олександрович",
                "телефон": "111222333",
                "корпоративний email": "sidorov@firm2.com",
                "назва посади": "інженер",
                "номер кабінету": "201",
                "Skype": "sidorov_skype"
            },
            {
                "ПІБ": "Коваленко Анна Василівна",
                "телефон": "444555666",
                "корпоративний email": "kovalenko@firm2.com",
                "назва посади": "аналітик",
                "номер кабінету": "202",
                "Skype": "kovalenko_skype"
            }
        ]
    },
    {
        "назва": "Фірма 3",
        "працівники": [
            {
                "ПІБ": "Михайленко Ольга Вікторівна",
                "телефон": "777888999",
                "корпоративний email": "mykhailenko@firm3.com",
                "назва посади": "аналітик",
                "номер кабінету": "301",
                "Skype": "mykhailenko_skype"
            }
        ]
    }
]

while True:
    print("\nОберіть опцію:")
    print("1. Додати працівника")
    print("2. Видалити працівника")
    print("3. Знайти працівника")
    print("4. Змінити дані працівника")
    print("5. Завершити програму")

    option = input("Ваш вибір: ")

    if option == "1":
        firm_name = input("Введіть назву фірми, в яку хочете додати працівника: ")
        firm_found = False
        for company in companies:
            if company["назва"] == firm_name:
                new_employee = {
                    "ПІБ": input("Введіть ПІБ працівника: "),
                    "телефон": input("Введіть телефон працівника: ")or None,
                    "корпоративний email": input("Введіть корпоративний email працівника: ")or None,
                    "назва посади": input("Введіть назву посади працівника: ")or None,
                    "номер кабінету": input("Введіть номер кабінету працівника: ")or None,
                    "Skype": input("Введіть Skype працівника: ")or None
                }
                company["працівники"].append(new_employee)
                print("Інформацію про працівника додано успішно.")
                firm_found = True
                break

        if not firm_found:
            new_firm = {
                "назва": firm_name,
                "працівники": []
            }
            new_employee = {
                "ПІБ": input("Введіть ПІБ працівника: "),
                "телефон": input("Введіть телефон працівника: ")or None,
                "корпоративний email": input("Введіть корпоративний email працівника: ")or None,
                "назва посади": input("Введіть назву посади працівника: ")or None,
                "номер кабінету": input("Введіть номер кабінету працівника: ")or None,
                "Skype": input("Введіть Skype працівника: ") or None
            }
            new_firm["працівники"].append(new_employee)
            companies.append(new_firm)
            print("Нову фірму створено, інформацію про працівника додано успішно.")
            print(companies)

        else:
            print("Фірми з такою назвою не знайдено.")

    if option == "2":
        firm_name = input("Введіть назву фірми, з якої хочете видалити працівника: ")
        employee_name = input("Введіть ПІБ працівника, якого хочете видалити: ")

        for company in companies:
            if company["назва"] == firm_name:
                for employee in company["працівники"]:
                    if employee["ПІБ"] == employee_name:
                        company["працівники"].remove(employee)
                        print("Інформацію про працівника успішно видалено.")
                        break
                else:
                    print("Прaцівника з таким ПІБ не знайдено.")
                break
        else:
            print("Фірми з такою назвою не знайдено.")

    if option == "3":
        firm_name = input("Введіть назву фірми, в якій хочете знайти працівника: ")
        employee_name = input("Введіть ПІБ працівника, якого хочете знайти: ")

        found = False
        for company in companies:
            if company["назва"] == firm_name:
                for employee in company["працівники"]:
                    if employee["ПІБ"] == employee_name:
                        print("Інформація про працівника:")
                        for key, value in employee.items():
                            print(f"{key}: {value}")
                        found = True
                        break
                break

        if not found:
            print("Прaцівника з таким ПІБ не знайдено.")

    if option == "4":
        firm_name = input("Введіть назву фірми, в якій хочете змінити дані працівника: ")
        employee_name = input("Введіть ПІБ працівника, дані якого хочете змінити: ")

        found = False
        for company in companies:
            if company["назва"] == firm_name:
                for employee in company["працівники"]:
                    if employee["ПІБ"] == employee_name:
                        print("Введіть нові дані працівника:")
                        employee["ПІБ"] = input("ПІБ: ")
                        employee["телефон"] = input("Телефон: ")
                        employee["корпоративний email"] = input("Корпоративний email: ")
                        employee["назва посади"] = input("Назва посади: ")
                        employee["номер кабінету"] = input("Номер кабінету: ")
                        employee["Skype"] = input("Skype: ")
                        print("Дані працівника змінено успішно.")
                        found = True
                        break
                break

        if not found:
            print("Прaцівника з таким ПІБ не знайдено.")

    elif option == "5":
        print("Завершення програми.")
        print(*companies)
        break

# Створіть програму «Книжкова колекція», яка зберігає інформацію про книги: автор,
# назва книги, жанр, рік випуску, кількість сторінок, видавництво.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.

# lib = [{"автор": "Джордж Оруелл",
#     "назва": "1984",
#     "жанр": "антиутопія",
#     "рік випуску": 1949,
#     "кількість сторінок": 328,
#     "видавництво": "Secker & Warburg"},
#        {"автор": "Джейн Остін",
#     "назва": "Гордість та упередження",
#     "жанр": "роман",
#     "рік випуску": 1813,
#     "кількість сторінок": 416,
#     "видавництво": "Thomas Egerton"},
#        {"автор": "Френсіс Скотт Фіцджеральд",
#     "назва": "Великий Гетсбі",
#     "жанр": "роман",
#     "рік випуску": 1925,
#     "кількість сторінок": 218,
#     "видавництво": "Charles Scribner's Sons"}]
#
# function = int(input("Натисніть 1, щоб додати, 2 - видалити, 3 - знайти, 4 - змінити дані: "))
#
# if function == 1:
#     lib.append({"автор": str(input("Введіть автор книги: ")) or None,
#                  "назва": str(input("Введіть назву книги: ")) or None,
#                  "жанр": str(input("Введіть жанр книги: ")) or None,
#                  "рік випуску": int(input("Введіть рік випуску книги: ")) if input("Введіть рік випуску книги: ") else None,
#                  "кількість сторінок": int(input("Введіть кількість сторінок книги: ")) if input("Введіть кількість сторінок книги: ") else None,
#                  "видавництво": str(input("Введіть видавництво книги: ")) or None})
#     print(lib)
# elif function == 2:
#     name = input("Введіть назву книжки:")
#     for book in lib:
#         if book["назва"] == name:
#             lib.remove(book)
#     print("Книжка видалена")
#     print(lib)
# elif function == 3:
#     name = input("Введіть назву книжки:") or None
#     autor = input("Введіть автора книжки:") or None
#     for book in lib:
#         if book["назва"] == name:
#             print(book)
#         elif book["автор"] == autor:
#             print(book)
#         else:
#             print("Книжка не знайдена")
#
# elif function == 4:
#     name = input("Введіть назву книжки:") or None
#     author = input("Введіть автора книжки:") or None
#     for book in lib:
#         if (name and book["назва"] == name) or (author and book["автор"] == author):
#             if name:
#                 new_name = input("Введіть нову назву книги:") or None
#                 if new_name:
#                     book["назва"] = new_name
#             if author:
#                 new_author = input("Введіть нового автора книги:") or None
#                 if new_author:
#                     book["автор"] = new_author
#             print("Дані книги оновлено:", book)
#             break
# else:
#     print("Unknown option")







