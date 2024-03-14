# Напишіть інформаційну систему «Співробітники» з аутентифікацією. Програма має забезпечувати введення,
# редагування та видалення даних про співробітника, пошук співробітника за прізвищем,
# виведення інформації про співробітників вказаного віку або прізвище яких починається
# з вказаної літери. Додайте функцію аутентифікації користувачів для доступу до програми.
# Аунтифіковані користувачі можуть робити всі дії, не аунтифіковані можуть тільки переглядати список,
# та фільтрувати співробітників з переглядом інформації
# Усі дані про співробітників та користувачів мають зберігатися у файлах. Зробіть
# можливість зберігати знайдену інформацію у файл, як і весь список співробітників
# (у процесі виконання програми — за командою користувача).
# Під час старту програми відбувається завантаження списку співробітників із зазначеного
# користувачем файлу.

def save_data(employees, users):
    with open("employees.txt", 'w') as f:
        for employee in employees:
            f.write(",".join(employee) + "\n")
    with open("users.txt", 'w') as f:
        for username, password in users.items():
            f.write(f"{username},{password}\n")

def load_data(employees_path, users_path):
    try:
        with open(employees_path, 'r') as f:
            employees = [line.strip().split(",") for line in f.readlines()]
    except FileNotFoundError:
        employees = []
        with open(employees_path, 'w'):
            employees_path.write(employees)
    try:
        with open(users_path, 'r') as f:
            users = dict(line.strip().split(",") for line in f.readlines())
    except FileNotFoundError as e:
        print("Could not open file")

    return employees, users


def sign_up(users,employees):
    username = input("Enter new username: ")
    if username in users:
        print("User already exists")
        return None
    password = input("Enter new password: ")
    users[username] = password
    print("User successfully signed up")
    save_data(employees, users)
    return username

def log_in(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("User successfully logged in")
        return username
    else:
        print("Wrong username or password")
        return None

def authenticate(users, employees):
    while True:
        choice = input("1. Log in\n2. Sign up\n3. Exit\nEnter choice: ")
        if choice == "1":
            username = log_in(users)
            if username:
                return username
        elif choice == "2":
            username = sign_up(users, employees)
            if username:
                return username
        elif choice == "3":
            return None
        else:
            print("Invalid choice. Try again.")

def search_employee(employees, search_type, search_query):
    if search_type == "surname":
        found_employees = [employee for employee in employees if employee[0].lower().startswith(search_query.lower())]
    elif search_type == "age":
        found_employees = [employee for employee in employees if employee[2] == search_query]
    else:
        print("Invalid search type.")
        return

    show_all_employees(found_employees, "Filtered employees")

def show_all_employees(employees, header="All employees:"):
    if not employees:
        print("No employees found")
        return
    print(header)
    print(f"{'Surname':<20}{'Name':<20}{'Age':<10}{'Position':<20}")
    print("-" * 70)
    for employee in employees:
        print(f"{employee[0]:<20}{employee[1]:<20}{employee[2]:<10}{employee[3]:<20}")
    print()

def add_employee(employees, users):
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    position = input("Enter position: ")
    employees.append((surname, name, age, position))
    print("Employee successfully added")
    save_data(employees, users)

def remove_employee(employees):
    surname = input("Enter surname: ")
    for employee in employees:
        if employee[0] == surname:
            employees.remove(employee)
            print("Employee successfully removed")
            return
    print("Employee not found")

def edit_employee(employees):
    surname = input("Enter surname: ")
    for i, employee in enumerate(employees):
        if employee[0] == surname:
            name = input("Enter name: ")
            age = input("Enter age: ")
            position = input("Enter position: ")
            employees[i] = (surname, name, age, position)
            print("Employee successfully edited")
            return
    print("Employee not found")

def main():
    employees_path = input("Введіть шлях до файлу: ") or input("")
    if employees_path == "":
        employees_path = "employees.txt"
    users_path = input("Введіть шлях до файлу: ") or input("")
    if users_path == "":
        users_path = "users.txt"
    employees, users = load_data(employees_path, users_path)
    current_user = authenticate(users, employees)
    if current_user is None:
        return

    while True:
        print("\nLogged in as", current_user)
        choice = input("1. Search employee\n2. Add employee\n3. Edit employee\n"
                       "4. Remove employee\n5. Show all employees\n6. Save data\n"
                       "7. Log out\n8. Exit\nEnter choice: ")

        if choice == "1":
            search_type = input("Enter search type (surname/age): ")
            search_query = input("Enter search query: ")
            search_employee(employees, search_type, search_query)
        elif choice == "2":
            add_employee(employees, users)
        elif choice == "3":
            edit_employee(employees)
        elif choice == "4":
            remove_employee(employees)
        elif choice == "5":
            show_all_employees(employees)
        elif choice == "6":
            save_data(employees, users)
        elif choice == "7":
            print("Logged out")
            current_user = authenticate(users, employees)
            if current_user is None:
                return
        elif choice == "8":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()



#Класна робота
# def save_data(books,users):
#     with open("books.txt", 'w') as f:
#         for book in books:
#             f.write(",".join(book)+"\n")
#     with open("users.txt", 'w') as f:
#         for user, password in books:
#             f.write(f"{user}, {password}\n")
#
# def load_data():
#     try:
#         with open("books.txt", 'r') as f:
#             books = [line.strip().split(",") for line in f.readlines()]
#     except FileNotFoundError as e:
#         books=[]
#     try:
#         with open("users.txt", 'r') as f:
#             users = [{line.split(",")[0]: line.split(",")[1].strip() for line in f.readlines()}]
#     except FileNotFoundError as f:
#         users =[]
#
# def sign_up(users):
#     username = input("Enter new username: ")
#     for user in users:
#         if user.get('username'):
#             print("User already exists")
#             return None
#     password = input("Enter new password: ")
#     users.append(dict(username= password))
#     print("User successfully signed up")
#     return username
#
# def log_in(users):
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if users.get(username) == password:
#         print("User successfully logged in")
#         return username
#     else:
#         print("Wrong username or password")
#         return None
#
# def search_book(books):
#     search_query = input("Enter search query(title, author, year, genre): ")
#     found_book ={
#         book for book in books if search_query in book[0].lower() or
#                                    search_query in book[1].lower() or
#                                    search_query in book[2].lower() or
#                                    search_query in book[3].lower()
#     }
#     print("Found")
#     show_all_book(found_book, "Filtered books")
#
# def show_all_book(books, header = "Available books:"):
#     if not books:
#         print("No books in the catalog")
#         return
#     else:
#         print(header)
#         print(f"{'Title':<30}{'Author':<25}{'Year':<10}{'Genre':<20}")
#         print("-" * 95)
#         for book in books:
#             title,author,year,genre = book
#             print(f"{title:<30}{author:<25}{year:<10}{genre:<20}")
#         print()
#
#
# def add_book(books):
#     title = input("Enter title: ")
#     author = input("Enter author: ")
#     year = input("Enter year: ")
#     genre = input("Enter genre: ")
#     books.append((title, author, year, genre))
#     print("Book successfully added")
#
# def remove_book(books):
#     title = input("Enter title: ")
#     for i, book in enumerate(books):
#         if book[0] == title:
#             del books[i]
#             print("Book successfully removed")
#             return
#     print("Book not found")
#
# def edit_book(books):
#     title = input("Enter title: ")
#     for i, book in enumerate(books):
#         if book[0] == title:
#             new_title = input("Enter title: ")
#             new_author = input("Enter author: ")
#             new_year = input("Enter year: ")
#             new_genre = input("Enter genre: ")
#             books[i] = (new_title or book[0], new_author or book[1], new_year or book[1], new_genre or book[1])
#             print("Book successfully edited")
#             return
#     print("Book not found")
#
#
# def main():
#     books, users = load_data()
#     current_user = None
#     while True:
#         if current_user:
#             print(f"\nLogged in as {current_user}")
#             choice = input("1. Search book.\n 2. Add book.\n 3.Edit book.\n "
#                            "4. Delete book.\n 5. Show all book.\n 6. Save data. 7. Log out.\n "
#                            "8.Exit.\n")
#             if choice == "1":
#                 search_book(books)
#             elif choice == "2":
#                 add_book(books)
#             elif choice == "3":
#                 edit_book(books)
#             elif choice == "4":
#                 remove_book(books)
#             elif choice == "5":
#                 show_all_book(books)
#             elif choice == "6":
#                 save_data(books, users)
#             elif choice == "7":
#                 break
#         else:
#             choice = input("1. Log in. 2. Sign up.\n 3.Search book.\n"
#                            "4. Show all books.\n 5.Exit.\n")
#             if choice == "1":
#                 current_user = log_in(users)
#             elif choice == "2":
#                 sign_up(users)
#             elif choice == "3":
#                 search_book(books)
#             elif choice == "4":
#                 show_all_book(books)
#             elif choice == "5":
#                 break

