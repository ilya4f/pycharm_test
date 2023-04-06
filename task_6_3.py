'''Реализовать базовый класс Worker (работник). Определить атрибуты: name, surname, position (должность),
income (доход); Последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}; Создать класс Position (должность) на базе класса Worker;
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income); Проверить работу примера на реальных данных:
создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.'''


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


vasya = Position('Вася', 'Сидоров', 'Программист', 100000, 20000)
print(vasya.get_full_name())
print(vasya.position)
print(vasya.get_total_income())
