print('Введите число x.')

try:
    x = float(input())
    y = 0

    if x < -11:
        y = 13 * x**4 - 110
    elif x >= -11 and x <=8:
        y = 26 * x**5 + x**3 - x**2
    else:
        y = 5 / 27 * x**2 - 51
    print(y)
except:
    print('Неверный формат введенных данных.')