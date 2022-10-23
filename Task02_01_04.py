# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

n = int(input('Введите натуральное число: '))
count = 2
number = n
lst = []
while count <= n:
    if n % count == 0:
        lst.append(count)
        n //= count
    else:
        count += 1
print(f"Простые множители числа {number}: {lst}")