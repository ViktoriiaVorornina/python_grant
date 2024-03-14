#На кришталик
# Маємо стос млинців різного радіусу. Єдина операція, яку ми можемо провести з ними — просунути лопатку між будь-якими
# двома млинцями і змінити їх порядок на зворотний. Відсортуйте цей стос знизу вгору, по спаданню радіусу млинців,
# за мінімальну кількість таких операцій.
from random import randint

#Не за мінімальну кількість (не зараховується виконаним) (просто тренувальне, оптимізую на досуге)
crepes = [randint(15, 50) for i in range(7)]  #Я не докінця не зрозуміла стос - це яка купка, тому буде 7 млинців.
n = len(crepes)
for i in range(n - 1):
    max_radius_index = i
    for j in range(i + 1, n):
        if crepes[j] > crepes[max_radius_index]:
            max_radius_index = j
    if max_radius_index != i:
        crepes = crepes[:i] + crepes[i:max_radius_index + 1][::-1] + crepes[max_radius_index + 1:]
        print("Поточний стан стосу млинців:", crepes)

print("Відсортований стан стосу млинців:", crepes)

# Маємо чотири списки цілих. Об’єднайте у п’ятому списку
# тільки ті елементи, які є унікальними для кожного списку.
# Отриманий результат відсортуйте за спаданням або зростанням в залежності від вибору користувача. Знайдіть значення,
# введене користувачем, з використанням бінарного пошуку|


# list1 = [3, 5, 7, 9, 11]
# list2 = [2, 5, 8, 11, 14]
# list3 = [1, 3, 5, 7, 9]
# list4 = [4, 6, 8, 10, 12]
#
# merged_list = list(list1 + list2 + list3 + list4)
# print(merged_list)
# merged_list.sort()
# descending = input("Введіть 1 для сортування за спаданням, або 2 для сортування за зростанням: ")
# if descending == 1:
#     merged_list.reverse()
# else:
#     merged_list.sort()
#
# print("Відсортований список унікальних значень:", merged_list)

# Напишіть програму «Книги». Створіть два списки з даними. Один список зберігає назви книг, другий — роки випуску.
# Реалізуйте меню для користувача:
# ■ відсортувати за назвою книг;
# ■ відсортувати за рокам випуску;
# ■ вивести список книг з назвами та роками випуску;
# ■ вихід

# titles = ["1984", "Гордість та упередження", "Великий Гетсбі", "Гаррі Поттер і філософський камінь", "Сто років самотності"]
# years = [1949, 1813, 1925, 1997, 1967]
#
# while True:
#     print("\nМеню:")
#     print("1. Відсортувати за назвою книг")
#     print("2. Відсортувати за роками випуску")
#     print("3. Вивести список книг з назвами та роками випуску")
#     print("4. Вихід")
#
#     choice = input("Оберіть опцію: ")
#
#     if choice == "1":
#         sorted_books = sorted(zip(titles, years), key=lambda x: x[0])
#         print("\nВідсортований список за назвою книг:")
#         for title, year in sorted_books:
#             print(f"{title} ({year})")
#
#     elif choice == "2":
#         sorted_books = sorted(zip(titles, years), key=lambda x: x[1])
#         print("\nВідсортований список за роками випуску:")
#         for title, year in sorted_books:
#             print(f"{title} ({year})")
#
#     elif choice == "3":
#         print("\nСписок книг з назвами та роками випуску:")
#         for title, year in zip(titles, years):
#             print(f"{title} ({year})")
#
#     elif choice == "4":
#         print("До побачення!")
#         break
#
#     else:
#         print("Некоректний ввід. Будь ласка, виберіть опцію з меню.")


# //////////////////////////
# Організація Бібліотеки.
# У вас є список книг у форматі (автор, назва, рік, видання)
# задача - написати наступні дії до списку:
# 1. Сортування книг - за автором, або за роком випуску
# 2. Пошук книги - по назві, за виданням, автору
# (якщо у книг видання однакові потрібно показати усі знайдені варіанти)
# 3. Фільтрація за Роком - користувач вводить рік та вибирає дію "Показади книги до даного року" або " після даного року"
# 4. Реалізувати меню для роботи з програмою

# books = [
#     ["Джордж Оруелл", "1984", 1949, "Secker & Warburg"],
#     ["Джейн Остін", "Гордість та упередження", 1813, "Thomas Egerton"],
#     ["Френсіс Скотт Фіцджеральд", "Великий Гетсбі", 1925, "Charles Scribner's Sons"],
#     ["Джоан Роулінг", "Гаррі Поттер і філософський камінь", 1997, "Bloomsbury Publishing"],
#     ["Габріель Гарсіа Маркес", "Сто років самотності", 1967, "Editorial Sudamericana"]
# ]
# while True:
#     print("\nМеню:")
#     print("1. Відсортувати за автором")
#     print("2. Відсортувати за роками випуску")
#     print("3. Пошук книги")
#     print("4. Фільтрація за роком")
#     print("5. Вихід")
#
#     choice = int(input("Оберіть опцію: "))
#
#     if choice == 1:
#         for i in range(len(books)):
#             for j in range(i + 1, len(books)):
#                 if books[i][0] > books[j][0]:
#                     books[i], books[j] = books[j], books[i]
#
#         print("Сортування за автором:")
#         for book in books:
#             print(book)
#
#     elif choice == 2:
#         for i in range(len(books)):
#             for j in range(i + 1, len(books)):
#                 if books[i][2] > books[j][2]:
#                     books[i], books[j] = books[j], books[i]
#
#         print("\nСортування за роком випуску:")
#         for book in books:
#             print(book)
#
#     elif choice == 3:
#         print("\nПошук книги:")
#         while True:
#             search = input("Введіть назву, автора або видання книги: ")
#             for book in books:
#                 if book[1] == search or book[0] == search or book[3] == search:
#                     print(book)
#                     break
#             else:
#                 print("Книга не знайдена.")
#
#     elif choice == 4:
#         year = int(input("Введіть рік: "))
#         filter_option = input("Оберіть опцію: '1 - Показати книги до даного року' або ' 2 - Показати книги після даного року': ")
#         if filter_option == '1':
#             filtered_books = [book for book in books if book[2] <= year]
#         elif filter_option == '2':
#             filtered_books = [book for book in books if book[2] > year]
#         else:
#             print("Неправильний вибір опції.")
#             continue
#
#         if filtered_books:
#             print("\nВідфільтровані книги:")
#             for book in filtered_books:
#                 print(book)
#         else:
#             print("Книги за вказаним роком не знайдено.")
#
#     elif choice == '5':
#         break
#
#     else:
#         print("Неправильний вибір. Будь ласка, введіть число від 1 до 5.")
