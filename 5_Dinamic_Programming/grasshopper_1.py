# coding=utf-8

""" Пусть кузнечик прыгает на одну или две точки вперед,
    а за прыжок в каждую точку необходимо заплатить определенную стоимость,
    различную для различных точек. Стоимость прыжка в точку i задается значением price[i] списка price.
    Необходимо найти минимальную стоимость маршрута кузнечика из точки 0 в точку n.
"""

# Напишите функцию calculate_min_cost(n, price) вычисления наименьшей стоимость достижения клетки n из клетки 1
""" Считаем, что в точку N, можно попасть из точки N-1 или точки N-2.
    Введем обозначения для стоимости посещения точки - price
                       для минимальной стоимости проходжения до данной точки от 1 - cost
    То есть достаточно посчитать минимальную стоимость достижения точек(cost) N-1 и N-2, выбрать меньшую из них,
    и прибавить стоимость посещения точки)(price) N.
    Выведем рекуррентную формулу: С(N) = min(C(N-1), C(N-2))
    Крайний случай: C[0] = None, C[1] = price[1], C[2] price[1] + price[2]
"""

def calculate_min_cost(n, price:list):
    C = [0, price[1], price[1] + price[2]] + [0] * (n-2)
    for i in range(3, n+1):
        C[i] = price[i] + C[i-1] if C[i-1] < C[i-2] else C[i-2]
    return C[n]

