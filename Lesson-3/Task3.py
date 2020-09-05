#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    """Возвращает сумму наибольших двух аргументов"""
    lst = [arg1, arg2, arg3]
    lst.sort()
    return lst[1] + lst[2]

print('my_func(1, 2, 3) = ', my_func(1, 2, 3))
print('my_func(1, 3, 2) = ', my_func(1, 3, 2))
print('my_func(2, 1, 3) = ', my_func(2, 1, 3))
print('my_func(2, 3, 1) = ', my_func(2, 3, 1))
print('my_func(3, 1, 2) = ', my_func(3, 1, 2))
print('my_func(3, 2, 1) = ', my_func(3, 2, 1))

