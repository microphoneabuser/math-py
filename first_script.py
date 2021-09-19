import math

print('Введите число x.')

try:
    x = float(input())
    g = 5/3 - math.atan(math.sqrt(2 - 2 * math.cos(x) - math.e ** (-(x/5))))
    print(g)
except:
    print('Неверный формат введенных данных.')
    