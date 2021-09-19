import random

# Функция с выбором действий программы
def main_menu():
    print('\n|\                        Что вы хотите сделать?                             /|\n')
    print('|\ Нажмите \'1\' если хотите выполнить заданные преобразования с числами x и y /|')
    print('|\ Нажмите \'2\' если хотите произвести действия с массивом, заданной длины    /|')
    print('|\ Нажмите \'q\' если хотите выйти                                             /|\n')
    answer = input()
    if answer == '1':
        count_first_exersice()
    elif answer == '2':
        count_second_exercise()
    elif answer == 'q':
        print('Пока!\n')
        exit()
    else:
        print('Вы ввели что-то непонятное...\n')
        main_menu()

# Функция, выполняющая преобразования с заданными числами (Задание №1)
def count_first_exersice():
    x, y = None, None
    print('Введите число x.')
    try:
        x = float(input())
    except:
        print('Неверный формат введенных данных.\n')
        main_menu()

    print('Введите число y.')
    try:
        y = float(input())
    except:
        print('Неверный формат введенных данных.\n')
        main_menu()

    if x < 0 and y < 0:
        x, y = my_abs(x, y)
    elif x < 0 or y < 0:
        x, y = multi_multi(x=x,y=y)
    elif x != 0 and y != 0 and (x < 0.5 or x > 2) and (y < 0.5 or y > 2):
        func = lambda x, z: x / z 
        x, y = func(x, 10), func(y, 10)
    print(f'\nx = {x}, y = {y}\n')
    main_menu()

# Функция, которая возвращает модули, переданных чисел
def my_abs(*args):
    return [abs(i) for i in args]

# Функция, которая умножает на 0.5 переданные числа
def multi_multi(**kwargs):
    return [kwargs[i] * 0.5 for i in kwargs]

# Функция, выполняющая действия с массивом, заданной длины (Задание №2)
def count_second_exercise():
    print('Введите количество элементов массива.')
    n = None
    try:
        n = int(input())
    except:
        print('Неверный формат введенных данных.\n')
        main_menu()

    # использую функцию round() просто для генерации чисел с меньшим количеством знаков после запятой
    # точность числа типа float в данном случае неважна
    arr = gen_arr(n)

    print('Исходный массив:' + str(arr) + '\n')

    odd_sum = get_sum_odd(arr)
    sum_sec = get_sum_sec(arr)

    print(f'Сумму элементов массива с нечетными номерами: {"%.2f" % odd_sum}')
    
    if sum_sec == None:
        print('Не найдено достаточно отрицательных элементов.')
    else:
        print(f'Сумма элементов массива, расположенных между первым и последним отрицательными элементами: {"%.2f" % sum_sec}\n')
    
    print(compress(arr))

    main_menu()

# Функция, вычисляющая сумму элементов массива с нечетными номерами
def get_sum_odd(arr):
    sum = 0
    for i in range(len(arr)):
        if i % 2 != 0:
            sum += arr[i]
    return sum

# Функция, вычисляющая сумму элементов массива, расположенных между первым и последним отрицательными элементами
def get_sum_sec(arr):
    first, last = None, None
    for i in range(len(arr)):
        if first == None and arr[i] < 0:
            first = i
        elif arr[i] < 0:
            last = i
    if not last:
        return None
    return sum(arr[first + 1:last])

# Функция, которая сжимает массив, удалив из него все элементы, модуль которых не превышает 1
# Освободившиеся в конце массива элементы заполнить нулями.
def compress(arr):
    for elem in arr:
        if abs(elem) <= 1:
            arr.remove(elem)
            arr.append(0)
    return arr

# Функция, которая генерирует массив
def gen_arr(n, min=-20.0, max=20.0, r=2):
    return [round(random.uniform(min, max), r) for i in range(n)]


print('\n/           /                Приветствую вас!                     \           \ ')
main_menu()