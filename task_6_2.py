'''Реализовать класс Road (дорога). Определить атрибуты: length (длина), width (ширина);
Значения атрибутов должны передаваться при создании экземпляра класса; Атрибуты сделать защищёнными;
Определить метод расчёта массы асфальта, Необходимого для покрытия всей дороги; Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
Проверить работу метода. Например: 20 м*5000 м*25 кг*5 см = 12500 т.'''


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass_per_sqm, thickness):
        asphalt_mass = self._length * self._width * mass_per_sqm * thickness
        return asphalt_mass


road = Road(20, 5000)
asphalt_mass = road.asphalt_mass(25, 5)
print(f"The necessary amount of asphalt for the road is {asphalt_mass:.0f} tons.")
