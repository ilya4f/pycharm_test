'''Реализуйте базовый класс Car. У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.'''


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {"налево" if direction == "left" else "направо"}')

    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.color} {self.name} превышает скорость! текущая скорость: {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.color} {self.name}: {self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.color} {self.name} превышает скорость! текущая скорость: {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.color} {self.name}: {self.speed} км/ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


car_1 = TownCar(70, 'черный', 'городская машина')
car_1.go()
car_1.show_speed()
car_1.turn('left')
car_1.stop()

car_2 = WorkCar(30, 'желтый', 'рабочая машина')
car_2.go()
car_2.show_speed()
car_2.turn('right')
car_2.stop()

car_3 = SportCar(100, 'красный', 'спортивная машина')
car_3.go()
car_3.show_speed()
car_3.turn('left')
car_3.stop()

car_4 = PoliceCar(80, 'бело-синий', 'полицейская машина')
car_4.go()
car_4.show_speed()
car_4.turn('right')
car_4.stop()
