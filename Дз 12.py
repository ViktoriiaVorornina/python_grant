# Маємо три кортежі цілих чисел. Знайдіть елементи, які
# є у всіх кортежах.

# tuple1 = (3,6,8,12,4,5)
# tuple2 = (45,64,3,4,9)
# tuple3 = (0, 10, 18, 19,20,4,3)
# common_elements = set(tuple1) & set(tuple2) & set(tuple3)
# result = tuple(common_elements)
# print(result)

# Маємо три кортежі цілих чисел. Знайдіть елементи, які
# унікальні для кожного списку
# tuple1 = (3,6,8,12,4,5)
# tuple2 = (45,64,3,4,9)
# tuple3 = (0, 10, 18, 19,20,4,3)
# unique_tuple1 = set(tuple1) - set(tuple2) - set(tuple3)
# unique_tuple2 = set(tuple2) - set(tuple1) - set(tuple3)
# unique_tuple3 = set(tuple3) - set(tuple1) - set(tuple2)
#
# print("Unique elements in tuple1:", unique_tuple1)
# print("Unique elements in tuple2:", unique_tuple2)
# print("Unique elements in tuple3:", unique_tuple3)

# Маємо три кортежі цілих чисел. Знайдіть елементи, які
# є в кожному з кортежів і знаходяться в кожному з них на тій
# самій позиції.

tuple1 = (0, 3, 6, 8, 12, 4, 5)
tuple2 = (0, 45, 64, 3, 4, 9)
tuple3 = (0, 10, 18, 19, 20, 4, 3)

common_elements = []
min_length = min(len(tuple1), len(tuple2), len(tuple3))

for i in range(min_length):
    if tuple1[i] == tuple2[i] == tuple3[i]:
        common_elements.append(tuple1[i])

print(tuple(common_elements))
