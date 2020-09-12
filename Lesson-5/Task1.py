# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

try:
    my_f = open("file1.txt", "w", encoding="utf-8")

    is_first = True
    while True:
        s = input('')
        if s != '':
            if not is_first:
                my_f.write('\n')
            my_f.write(s)
            is_first = False
        else:
            break
finally:
    my_f.close()