import pandas as pd

filename = 'data.txt'

# Функция с выбором действий программы
def main_menu():
    print('\n|\                        Что вы хотите сделать?                             /|\n')
    print('|\ Нажмите \'1\' если хотите добавить запись о спортсмене                      /|')
    print('|\ Нажмите \'2\' если хотите удалить запись о спортсмене                       /|')
    print('|\ Нажмите \'3\' если хотите вывести список спортсменов                        /|')
    print('|\ Нажмите \'4\' если хотите вывести таблицу спортсменов                       /|')
    print('|\ Нажмите \'q\' если хотите выйти                                             /|\n')
    answer = input()
    if answer == '1':
        add_person()
    elif answer == '2':
        del_person()
    elif answer == '3':
        show_persons()
    elif answer == '4':
        show_table()
    elif answer == 'q':
        exit()
    else:
        print('Вы ввели что-то непонятное...\n')
        main_menu()

# Функция, которая добавляет спортсмена в список
def add_person():
    string = collect_string()
    if check_id(string.split('|')[0]):
        with open(filename, 'a') as f:
            f.write(string + '\n')
        print('\nЗапись успешно добавлена!')
        main_menu()
    else:
        print('\nСпортсмен с таким ИД уже существует.')
        main_menu()

# Функция, которая удаляет спортсмена из списка
def del_person():
    id = input('\nВведите ИД спортсмена: ')
    try:
        id = int(id)
    except:
        print('Неверный формат введенных данных.\n')
        main_menu()
    if check_id(id):
        f = open(filename).readlines()
        i = 0
        while True:
            line = f[i]
            if not line:
                break
            if line.split('|')[0] == str(id):
                f.pop(i)
                with open(filename,'w') as F:
                    F.writelines(f)
                break
            i += 1   
        print('\nЗапись успешно удалена!') 
    else:
        print('Нет спортсмена с таким ИД. :(\n')
    main_menu()

# Функция, которая показывает список спортсменов
def show_persons():
    print()
    for line in open(filename, 'r').readlines():
        line_arr = line.split('|')
        weight = line_arr[7].replace('\n', '')
        print(f'ИД: {line_arr[0]}; ' + \
            f'Страна: {line_arr[1]}; ' + \
            f'Команда: {line_arr[2]}; ' + \
            f'ФИО: {line_arr[3]}; ' + \
            f'Номер: {line_arr[4]}; ' + \
            f'Возраст: {line_arr[5]}; ' + \
            f'Рост: {line_arr[6]}; ' + \
            f'Вес: {weight}')
    main_menu()

# Функция, которая показывает таблицу спортсменов
def show_table():
    id_arr = []
    country_arr = []
    team_arr = []
    fio_arr = []
    number_arr = []
    age_arr = []
    height_arr = []
    weight_arr = []
    for line in open(filename, 'r').readlines():
        line_arr = line.split('|')
        id_arr.append(line_arr[0])
        country_arr.append(line_arr[1])
        team_arr.append(line_arr[2])
        fio_arr.append(line_arr[3])
        number_arr.append(line_arr[4])
        age_arr.append(line_arr[5])
        height_arr.append(line_arr[6])
        weight_arr.append(line_arr[7].replace('\n',''))
    print()
    print(pd.DataFrame(
        {"ИД": id_arr,
        "Страна": country_arr,
        "Команда": team_arr,
        "ФИО": fio_arr,
        "Номер": number_arr,
        "Возраст": age_arr,
        "Рост": height_arr,
        "Вес": weight_arr},
        index=None))
    main_menu()

# Функция, которая собирает введенные пользователем данные в строку, готовую для записи в файл
def collect_string():
    id = input('\nВведите ИД: ')
    try:
        id = int(id)
    except:
        print('Неверный формат введенных данных.):\n')
        main_menu()
    country = input('Введите страну: ')
    team = input('Введите команду: ')
    fio = input('Введите ФИО: ')
    number = input('Введите номер: ')
    try:
        number = int(number)
    except:
        print('Неверный формат введенных данных.):\n')
        main_menu()
    age = input('Введите возраст: ')
    try:
        age = int(age)
    except:
        print('Неверный формат введенных данных.):\n')
        main_menu()
    height = input('Введите рост: ')
    try:
        height = int(height)
    except:
        print('Неверный формат введенных данных.):\n')
        main_menu()
    weight = input('Введите вес: ')
    try:
        weight = int(weight)
    except:
        print('Неверный формат введенных данных.):\n')
        main_menu()
    
    return f'{id}|{country}|{team}|{fio}|{number}|{age}|{height}|{weight}'

# Функция, которая проверяет наличие спортсмена в списке
def check_id(id):
    f = open(filename)
    while True:
        line = f.readline()
        if not line:
            return True
        if line.split('|')[0] == id:
            return False

        
print('\n/           /                Приветствую вас!                     \           \ ')
main_menu()