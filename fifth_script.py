from random import randrange
import math

y = [randrange(-100, 100) for i in range(25)] 

print('Исходный массив: ' + str(y))

r = []
for elem in y:
    r.append((5 * elem + math.cos(elem)**2) / 2.35)

print('Результат: ')

for elem in r:
    print("%.2f" % elem, end=" ")