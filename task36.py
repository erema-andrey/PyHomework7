# # Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# # копией values.
# values = [1, 23, 42, 'asdfg']
# transformation = lambda x: x
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

"""Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту,
по которой вращается самая далекая планета. Круговые орбиты не учитывайте.
Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения."""
from math import pi


def find_farthest_orbit(list_of_orbits: list):
    for orbit in list_of_orbits:
        # если площадь текущей орбиты = максимальной (максимальную находим в списке площадей всех орбит, кроме круговых)
        if orbit[0] * orbit[1] * pi == max(map(lambda lst: lst[0] * lst[1] * pi,
                                               filter(lambda lst: lst[0] != lst[1], list_of_orbits))):
            return orbit


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

