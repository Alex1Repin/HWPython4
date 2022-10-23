# Задайте последовательность цифр. Напишите программу, которая выведет 
# список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from random import randrange

def numbers(n): 
    numbers = [randrange(0, n)]
    for i in range(1, n):
        numbers.append(randrange(0, n))
    return (numbers)

roll = (numbers(10))
print(roll)

lst = roll
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(f"Список неповторяющихся элементов: {new_lst}")