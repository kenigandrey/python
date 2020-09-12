# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

try:
    my_f1 = open("text_4.txt", "r", encoding="utf-8")
    my_f2 = open("text_4_new.txt", "w", encoding="utf-8")
    for line in my_f1:
        line = line.replace("One", "Один")
        line = line.replace("Two", "Два")
        line = line.replace("Three", "Три")
        line = line.replace("Four", "Четыре")
        my_f2.write(line)
finally:
    my_f1.close()
    my_f2.close()