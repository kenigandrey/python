# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def __init__(self):
        self.title = 'ручка'

    def draw(self):
        print(f'{self.title}. Запуск отрисовки класса Pen')

class Pencil(Stationery):

    def __init__(self):
        self.title = 'карандаш'

    def draw(self):
        print(f'{self.title}. Запуск отрисовки класса Pencil')

class Handle(Stationery):

    def __init__(self):
        self.title = 'маркер'

    def draw(self):
        print(f'{self.title}. Запуск отрисовки класса Handle')


Stationery_1 = Stationery('перо')
Stationery_1.draw()

print()

Pen_1 = Pen()
Pen_1.draw()

print()

Pencil_1 = Pencil()
Pencil_1.draw()

print()

Handle_1 = Handle()
Handle_1.draw()