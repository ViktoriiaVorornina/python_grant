# Task 1
# number = (int(input("Введіть число: ")))
# for i in range(1, 10):
#     print(f"\t\t\t{number} * {i} = ", number * i)


# Task 2
# гривні, долари, євро (курс Приватбанку на 21.12.2023)
money = int(input("Натисніть 1, якщо у вас гривні, 2 - долари, 3 - євро: "))
summa = int(input("Введіть сумму грошей: "))
if money == 1:
    option = int(input("Натисніть 1, якщо ви хочете отримати долари, 2 - євро: "))
    if option == 1:
        result = summa / 37.9
        print(f"Маючи {summa} грн, Ви отримаєте {result:.2f} $ ")
    elif option == 2:
        result = summa / 41.9
        print(f"Маючи {summa} грн, Ви отримаєте {result:.2f} євро ")
    else:
        print("Обрали некоректну опцію.")
elif money == 2:
    option = int(input("Натисніть 1, якщо ви хочете отримати гривні, 2 - євро: "))
    if option == 1:
        result = summa * 37.4
        print(f"Маючи {summa} $, Ви отримаєте {result:.2f} грн ")
    elif option == 2:
        result = summa * 0.9
        print(f"Маючи {summa} $, Ви отримаєте {result:.2f} євро ")
    else:
        print("Обрали некоректну опцію.")
elif money == 3:
    option = int(input("Натисніть 1, якщо ви хочете отримати гривні, 2 - долари: "))
    if option == 1:
        result = summa * 40.9
        print(f"Маючи {summa} євро, Ви отримаєте {result:.2f} грн ")
    elif option == 2:
        result = summa * 1.1
        print(f"Маючи {summa} євро, Ви отримаєте {result:.2f} $ ")
    else:
        print("Обрали некоректну опцію.")

else:
    print("Такої валюти в нашому банку немає.")

# Task 3
# lim1 = (int(input("Введіть початкову межу: ")))
# lim2 = (int(input("Введіть кінцеву межу: ")))
# number = (int(input("Введіть число: ")))
# while number not in range(lim1, lim2):
#     number = (int(input("Введіть число: ")))
# for i in range(lim1, lim2):
#     if lim1 < number < lim2 and number != i:
#         print(i, end="\t")
#     elif number == i:
#         print(f" !{number}!", end="\t")
