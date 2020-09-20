#Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def calc_fabric(self):
        pass

class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        if V > 10:
            self.__V = 10
        else:
            self.__V = V

    @property
    def calc_fabric(self):
        return self.V/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    def calc_fabric(self):
        return 2*self.H + 0.3


print('Пальто:')
Coat1 = Coat(1)
print('V = ', Coat1.V)
print('calc_fabric = ', Coat1.calc_fabric)

print()

Coat1.V = 15
print('V = ', Coat1.V)
print('calc_fabric = ', Coat1.calc_fabric)


print()

print('Костюм:')
Suit1 = Suit(1)
print('H = ', Suit1.H)
print('calc_fabric() = ', Suit1.calc_fabric())