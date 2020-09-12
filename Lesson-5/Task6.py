# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                     Физика:   30(л)   —   10(лаб)
#                     Физкультура:   —   30(пр)   —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def f_num(arg):
    lst = list(arg)
    res = ''
    for i in lst:
        if str(i).isdigit():
            res += i
    if res == '':
        return 0
    else:
        return float(res)

try:
    my_f = open("text_6.txt", "r", encoding="utf-8")
    my_dict = dict()
    for line in my_f:
        lst_str = line.split(':')
        lst_cnt = lst_str[1].split(' ')
        my_dict.update({lst_str[0]: sum(list(map(f_num, lst_cnt)))})
    print(my_dict)
finally:
    my_f.close()