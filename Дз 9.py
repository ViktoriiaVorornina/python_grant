# #Два списки цілих заповнюються випадковими числами.
# Сформуйте третій список, який містить:
# ■ елементи обох списків;
# ■ елементи обох списків без повторень;
# ■ елементи, спільні для двох списків;
# ■ тільки унікальні елементи кожного зі списків;
# ■ тільки мінімальне та максимальне значення кожного зі
# списків.

import random
list1 = [random.randint(0,15) for i in range(7)]
list2 = [random.randint(0,20) for i in range(7)]
list3 = list1 + list2
print(f"Елементи обох списків - {list3}")
list4 = list(set(list3))
print(f"Елементи обох списків без повторень - {list4}")
list5 = list(set([x for x in list1 if x in list2]))
print(f"Елементи, спільні для двох списків - {list5}")
list6 = list(set(list1) - set(list2))
print(f"Елементи тільки унікальні 1-го списка - {list6}")
list7 = list(set(list2) - set(list1))
print(f"Елементи тільки унікальні 2-го списка - {list7}")
print(f"Мінімальне значення першого списку - {min(list1)}, максимальне значення першого списку - {max(list1)}, "
      f"мінімальне значення другого списку - {min(list2)}, максимальне значення другого списку - {max(list2)}")









#Класна робота
#
# words = ["port", "lampe", "choice", "life"]
# word = random.choice(words)
# word_completion = "_"*len(word)
# print(word_completion)
#
# guessed_letters = []
# guessed = False
# tries = 6
# print("Game guess the word")
#
# while not guessed and tries > 0:
#     print(word_completion)
#     guess = input("Guess a letter or word: ").lower()
#
#     if len(guess) == 1 and guess.isalpha():
#         if guess in guessed_letters:
#             print("Already guessed", guess)
#         elif guess not in word:
#             print("Wrong answer", guess)
#             tries -= 1
#             guessed_letters.append(guess)
#         else:
#             print("Correct answer", guess)
#             guessed_letters.append(guess)
#             word_as_list = list(word_completion)
#             indices = [i for i, letter in enumerate(word) if letter == guess]
#             for i in indices:
#                 word_as_list[i] = guess
#             word_completion = "".join(word_as_list)
#             if '_' not in word_completion:
#                 guessed = True
#     elif len(guess) == len(word) and guess.isalpha():
#         if guess == word:
#             guessed = True
#             word_completion = word_completion.replace(guess)
#         else:
#             print("Wrong answer", guess)
#             tries -= 1
#     else:
#         print("Invalid answer", guess)
#
#     print(f"Attempts left: {tries}")
#
# if guessed:
#     print("You won!")


# У списку цілих, заповненому випадковими числами,
# розрахуйте:
# ■ Суму від’ємних чисел.
# ■ Суму парних чисел.
# ■ Суму непарних чисел.
# Добуток елементів з індексами, кратними 3.
# ■ Добуток елементів між мінімальним та максимальним
# елементом.
# ■ Суму елементів, що знаходяться між першим та останнім додатним елементом.

from random import randint
# numbers = []
# for i in range(10):
#     numbers.append(randint(-10, 10))
# print(numbers)
# sum_e = sum(x for x in numbers if x % 2 == 0)
# sum_n = sum(x for x in numbers if x < 0)
# sum_neparni = sum(x for x in numbers if x % 2 != 0)
# mult = 1
# for i in range(0, len(numbers), 3):
#     mult *= numbers[i]
#
# min = numbers.index(min(numbers))
# max = numbers.index(max(numbers))
# print(min,max)
# if min > max:
#     min, max = max, min
#
# mult_2 = 1
# for i in range(min, max + 1, 3):
#     mult_2 *= numbers[i]
#
# start_i = None
# end_i = None
# for i in range(0,len(numbers)):
#     if numbers[i] > 0:
#         start_i = i
#         break
#
# for i in range(len(numbers)-1, 0, -1):
#     if numbers[i] > 0:
#         end_i = i
#         break
#
#
# print(f"Сума парних чисел = {sum_e}")
# print(f"Сума від'ємних чисел = {sum_n}")
# print(f"Сума непарних чисел = {sum_neparni}")
# print(f"Добуток з індексами, кратними 3 = {mult}")
# print(f"Добуток елементів між мінімальним та максимальним елементом = {mult_2}")
# print(sum(numbers[start_i+1:end_i]))

