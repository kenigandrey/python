#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

try:
    my_f = open("file5.txt", "w", encoding="utf-8")
    my_list = (str(randint(0, 10)) for i in range(10))
    my_f.write(' '.join(my_list))
finally:
    my_f.close()

try:
    my_f = open("file5.txt", "r", encoding="utf-8")
    lst = my_f.read().split(" ")
    lst2 = list(map(float, lst))
#    print(lst2)
    print(f"Сумма: {sum(lst2)}")
finally:
    my_f.close()