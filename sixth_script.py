import random

y = []
neg = 0
for i in range(0, 3):
    li = list()
    for j in range(0, 4):
        el = random.randint(-100, 100)
        li.append(el)
        if el < 0:
            neg = neg + 1
    y.append(li)

print('Исходная матрица: ' + str(y))
print('Количество отрицательных элементов: ' + str(neg))