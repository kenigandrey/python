#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1   ООО   10000   5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.

import json

try:
    my_f = open("text_7.txt", "r", encoding="utf-8")
    my_dict = dict()
    lst_profit = list()
    for line in my_f:
        lst_str = line.split(' ')
        profit = float(lst_str[2]) - float(lst_str[3])
        if profit >= 0:
            lst_profit.append(profit)
        my_dict.update({lst_str[0]: profit})
    my_dict2 = {"average_profit": sum(lst_profit)/len(lst_profit)}

    lst = [my_dict, my_dict2]
#    print(lst)

    with open("my_file.json", "w", encoding="utf-8") as write_f:
        json.dump(lst, write_f, indent=4, ensure_ascii=False)
#    print(my_dict)
#    print(my_dict2)
finally:
    my_f.close()