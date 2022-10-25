# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до
# ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную 
# итерацию степени
# Записываем результат в файл.
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


from random import randint

def numbers(k, n): 
    numbers = [randint(-n, n)]
    for i in range(0, k):
        numbers.append(randint(-n, n))
    return numbers

def degree(k): 
    deg = []
    num = k
    for i in range(0, k+1):
        deg.append(num)
        num -=1
    return deg

def polinomial(rol, deg):
    lst1 = rol
    lst2 = deg
    st = ''
    for i in range(len(lst2)):
        if i != len(lst2)-1 and lst1[i] != 0 and i != len(lst2)-2:
            st += f'{lst1[i]}x^{lst2[i]}'
            if lst1[i+1] != 0:
                st += ' + '
        elif i == len(lst2)-2 and lst1[i] != 0:
            st += f'{lst1[i]}x'
            if lst1[i+1] != 0:
                st += ' + '
        elif i == len(lst2) - 1 and lst1[i] != 0:
                st += f'{lst1[i]} = 0'
        elif i == len(lst2) -1 and lst2[i] == 0:
                st += ' = 0'
    return st

def write_file(fl):
     with open ('polinomial.txt', 'w') as data:
          data.write(fl)

k = int(input("Введите натуральную степень k = "))
n = 100
roll = numbers(k, n)
degre = degree(k)
polinom = polinomial(roll, degre)

print(roll)#создание коэффициента многочлена
print(degree(k))#создание степени многочлена
print(polinom)#создание многочлена
write_file(polinom)
