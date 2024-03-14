# Напишіть функцію, яка виводить на екран форматований
# текст, наведений нижче:
# “Don’t compare yourself with anyone in this world…
#  if you do so, you are insulting yourself.”
# Bill Gates

# def main(text1, text2, autor):
#     formatted_text = f'“{text1}\n\t{text2}”\n\t\t\t\t\t\t\t\t{autor}'
#     print(formatted_text)
#
# text = main("Don’t compare yourself with anyone in this world…", "if you do so, you are insulting yourself."
#             ,"Bill Gates")

# Напишіть функцію, яка приймає два числа як параметр
# і відображає усі парні числа між ними.

# def eval(first: int, second: int):
#     list1 = []
#     if first > second:
#         first, second = second, first
#     for i in range(first, second):
#         if i % 2 == 0:
#             list1.append(i)
#     return list1
#
# print(eval(int(input("Введіть першу границю: ")), int(input("Введіть другу границю: "))))


# Напишіть функцію, яка відображає порожній або заповнений квадрат із певним символом. Функція приймає в якості параметрів довжину сторони квадрата, символ та змінну
# логічного типу:
# ■ якщо вона дорівнює True, квадрат заповнений;
# ■ якщо False, квадрат порожній.

# def carre(len: int, symbol: str, status = True):
#     if status:
#         for i in range(len):
#             print(symbol*len, end="\n")
#     else:
#         print(symbol * len)
#         for _ in range(len - 2):
#             print(symbol + '   ' * (len - 2) + symbol)
#         print(symbol * len)
#
#
# carre(7, " * ", False)


# Напишіть функцію, яка повертає мінімальне з п’яти чисел.
# Числа передаються як параметри.

# def minimal(*args):
#     min = args[0]
#     for i in range(len(args)):
#         if args[i] < min:
#             min = args[i]
#     return min
#
# print(minimal(23, 19, 4, 80, 99, 106))


# Напишіть функцію, яка повертає добуток чисел у зазначеному діапазоні. Межі діапазону передаються як параметри.
# Якщо межі діапазону переплутані (наприклад, 5 — верхня
# межа, 25 — нижня межа), їх треба поміняти місцями.

# def dobutok(first: int, second: int):
#     if first > second:
#         first, second = second, first
#     dob = 1
#     for i in range(first, second+1):
#         dob *= i
#     return dob
#
# print(dobutok(int(input("Введіть першу границю: ")), int(input("Введіть другу границю: "))))

# Напишіть функцію, яка підраховує кількість цифр у числі.
# Число передається як параметр. Поверніть з функції отриману
# кількість цифр. Наприклад, якщо передали 3456, кількість
# цифр буде 4

# def num_chiffre(chiffre: int):
#     count = 0
#     while chiffre > 0:
#         count += 1
#         chiffre //= 10
#     return count
#
# print(num_chiffre(int(input("Введіть число: "))))

# Напишіть функцію, яка перевіряє число на паліндром.
# Число передається як параметр. Якщо число є паліндромом,
# поверніть з функції true, якщо ні — false.
# «Паліндром» — це число, в якому перша частина цифр
# дорівнює другій перевернутій частини цифр. Наприклад,
# 123321 — паліндром (перша частина 123, друга 321, яка після
# перевороту стає 123), 546645 — паліндром, а 421987 — не
# паліндром.

def palindrome(number):
    number = str(number)
    for i in range(len(number) // 2):
        if number[i]!= number[len(number) - i - 1]:
            return False
    return True

print(palindrome(int(input("Введіть число: "))))