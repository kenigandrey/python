# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_func():
    """Возвращает сумму чисел введенных чисел через пробел.
       Некорректные числа не учитываются.
       Символ для завершения ввода - q
    """
    res = 0
    while True:
        s = input('введите числа через пробел = ')
        lst = s.split()
        for i in lst:
            if i == 'q':
                print(f"Итоговая сумма: {res}")
                return
            else:
                try:
                    res += float(i)
                except ValueError:
                    pass

        print(f"Предварительная сумма: {res}")

my_func()
