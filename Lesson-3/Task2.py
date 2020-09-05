# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(arg_name, arg_surname, arg_year, arg_city, arg_email, arg_phone):
    """Возвращает информацию о пользователе одной строкой"""
    lst = dict()
    lst.update({'имя': arg_name})
    lst.update({'фамилия': arg_surname})
    lst.update({'год рождения': arg_year})
    lst.update({'город проживания': arg_city})
    lst.update({'email': arg_email})
    lst.update({'телефон': arg_phone})
    return lst

print(my_func(arg_name = 'Гарри', arg_surname = 'Поттер', arg_year = 1980, arg_city = 'Лондон', arg_email = 'harrypotter@mail.ru', arg_phone = 123456))
