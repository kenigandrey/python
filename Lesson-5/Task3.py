# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

from builtins import map

try:
    my_f = open("text_3.txt", "r", encoding="utf-8")
    lst = my_f.read().split("\n")
    my_dict = dict()
    for line in lst:
        lst2 = line.split(' ')
        my_dict.update({lst2[0]: float(lst2[1])})
    print(f"Средняя величина дохода = {sum(my_dict.values())/len(my_dict.values())}")
    print('Сотрудники с окладом менее 20000: ', [i for i in my_dict if my_dict.get(i) < 20000])
finally:
    my_f.close()