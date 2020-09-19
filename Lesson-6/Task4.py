# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed = 0

    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self._is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'{self.name}. Машина поехала со скоростью {speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'{self.name}. Машина остановилась')

    def turn(self, direction):
        print(f'{self.name}. Машина повернула на ' + direction)

    def show_speed(self):
        print(f'{self.name}. Текущая скорость {self.speed} км/ч')

    def show_info(self):
        print(f'{self.name}. name = {self.name}, color = {self.color}, speed = {self.speed} км/ч, is_police = {self._is_police}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.name}. Превышена скорость в 60 км/ч')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.name}. Превышена скорость в 40 км/ч')

class PoliceCar(Car):
    pass


TownCar_1 = TownCar('TownCar', 'черный')
TownCar_1.go(30)
TownCar_1.go(100)
TownCar_1.show_speed()
TownCar_1.turn('лево')
TownCar_1.turn('право')
TownCar_1.stop()
TownCar_1.show_info()

print()

SportCar_1 = SportCar('SportCar', 'белый')
SportCar_1.go(30)
SportCar_1.go(100)
SportCar_1.show_speed()
SportCar_1.turn('лево')
SportCar_1.turn('право')
SportCar_1.stop()
SportCar_1.show_info()

print()

WorkCar_1 = WorkCar('WorkCar', 'синий')
WorkCar_1.go(30)
WorkCar_1.go(100)
WorkCar_1.show_speed()
WorkCar_1.turn('лево')
WorkCar_1.turn('право')
WorkCar_1.stop()
WorkCar_1.show_info()

print()

PoliceCar_1 = PoliceCar('PoliceCar', 'желтый', True)
PoliceCar_1.go(30)
PoliceCar_1.go(100)
PoliceCar_1.show_speed()
PoliceCar_1.turn('лево')
PoliceCar_1.turn('право')
PoliceCar_1.stop()
PoliceCar_1.show_info()
