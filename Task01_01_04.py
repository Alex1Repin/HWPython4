# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
# !!ВНИМАНИЕ
# !!! не использовать константу math.pi


d = input('Введите заданную точность: ')
d = d[2:len(d)]
lst = list(d)
i = int(len(lst))
print(355*10**i//113/10**i)
#для 30 знака и более print(103993*10**i//33102/10**i)

d = input('Введите заданную точность: 0.1')
lst = list(d)
i = len(lst)
print(i)
#Почему количество символов 127