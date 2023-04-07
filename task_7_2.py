'''Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта - одежда (класс Clothes). К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: v и h, соответственно. Для определения расхода ткани по каждому типу одежды
использовать формулы: для пальто (v/6.5 + 0.5), для костюма (2*h + 0.3).
Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property'''

from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothing):
    def __init__(self, size):
        self._size = size

    @property
    def fabric_consumption(self):
        return self._size / 6.5 + 0.5


class Suit(Clothing):
    def __init__(self, height):
        self._height = height

    @property
    def fabric_consumption(self):
        return 2 * self._height + 0.3


class ClothingFactory:
    @staticmethod
    def create_clothing(clothing_type, param):
        if clothing_type == "coat":
            return Coat(param)
        elif clothing_type == "suit":
            return Suit(param)


items = [
    ClothingFactory.create_clothing("coat", 50),
    ClothingFactory.create_clothing("suit", 165),
    ClothingFactory.create_clothing("coat", 46),
    ClothingFactory.create_clothing("suit", 170)
]

total_fabric_consumption = sum(item.fabric_consumption for item in items)
print(f"Total fabric consumption: {total_fabric_consumption}")
