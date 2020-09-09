# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


from itertools import count
from itertools import cycle

print('итератор, генерирующий целые числа, начиная с указанного:')
beg_num = 100
end_num = 120

for i in count(beg_num):
    if i > end_num:
        break
    else:
        print(i)

print('итератор, повторяющий элементы некоторого списка, определенного заранее:')
end_cnt = 8
i = 1
for el in cycle(['Один', 'Два', 'Три', 'Четыре', 'Пять']):
    if i > end_cnt:
        break
    print(el)
    i += 1