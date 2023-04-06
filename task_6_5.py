'''Реализовать класс Stationery (канцелярская принадлежность). Определить в нём атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»; Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер); В каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашем {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером {self.title}")


stationery = Stationery('Гусиное перо')
stationery.draw()

pen = Pen('Гелевая')
pen.draw()

pencil = Pencil('Учебный')
pencil.draw()

handle = Handle('Для белой доски')
handle.draw()
