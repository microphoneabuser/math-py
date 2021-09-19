print('Введите строку.')
l = input()

if len(l) > 10:
    for ch in l:
        if ch.isdigit():
            l = l.replace(ch,'')
print(l)